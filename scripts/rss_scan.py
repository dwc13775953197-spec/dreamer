#!/usr/bin/env python3
"""
Dreamer RSS Scanner v2
- 用 curl 通过代理抓取 RSS，Python 解析 XML。
- 绕过 Go/urllib 的私有地址限制。
- ⚠️ socks5 代理不可靠（Vercel challenge），已改为直连。
"""

import json
import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

# ─── 配置 ───────────────────────────────────────────
PROXY = None  # socks5 proxy unreliable — Vercel challenge blocks it. Use direct curl.
DB_PATH = os.path.expanduser("~/hermes_dreamer/rss-digest")
HOURS_BACK = 24

FEEDS = {
    "lesswrong": {
        "url": "https://www.lesswrong.com/feed.xml",
        "domain": "rationality/cognition/AI safety",
    },
    "thegradient": {
        "url": "https://thegradient.pub/rss/",
        "domain": "ML research/deep dives",
    },
    "alignmentforum": {
        "url": "https://www.alignmentforum.org/feed.xml",
        "domain": "AI alignment",
    },
}
# ────────────────────────────────────────────────────


def fetch_url(url: str) -> bytes:
    """用 curl 获取 URL 内容（直连，不走代理）"""
    cmd = ["curl", "-sL", "--connect-timeout", "15", "--max-time", "30",
           "-H", "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Dreamer-RSS/1.0", url]
    result = subprocess.run(cmd, capture_output=True, timeout=35)
    if result.returncode != 0:
        raise RuntimeError(f"curl failed: {result.stderr.decode()[:200]}")
    return result.stdout


def parse_date(date_str: str | None) -> datetime | None:
    """解析各种 RSS/Atom 日期格式"""
    if not date_str:
        return None
    date_str = date_str.strip()
    formats = [
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S GMT",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%d %H:%M:%S",
    ]
    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue
    return None


def parse_feed(xml_bytes: bytes, feed_name: str) -> list[dict]:
    """解析 RSS/Atom XML，返回文章列表"""
    articles = []
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError as e:
        return [{"error": f"XML parse error: {e}"}]

    ns = {}
    if root.tag.startswith("{"):
        uri = root.tag.split("}")[0].lstrip("{")
        ns = {"atom": uri}

    # Atom feed
    if root.tag.endswith("feed") or "feed" in root.tag:
        entries = root.findall("atom:entry", ns) or root.findall("entry")
        for entry in entries:
            title_el = entry.find("atom:title", ns) or entry.find("title")
            title = title_el.text.strip() if title_el is not None and title_el.text else "No title"

            link_el = entry.find("atom:link", ns) or entry.find("link")
            link = ""
            if link_el is not None:
                link = link_el.get("href", "") or (link_el.text or "")

            summary_el = entry.find("atom:summary", ns) or entry.find("summary")
            if summary_el is None:
                summary_el = entry.find("atom:content", ns) or entry.find("content")
            summary = ""
            if summary_el is not None and summary_el.text:
                summary = summary_el.text.strip()[:300]

            date_el = entry.find("atom:published", ns) or entry.find("published")
            if date_el is None:
                date_el = entry.find("atom:updated", ns) or entry.find("updated")
            pub_date = parse_date(date_el.text if date_el is not None and date_el.text else None)

            articles.append({
                "title": title,
                "link": link,
                "summary": summary,
                "published": pub_date.isoformat() if pub_date else None,
                "published_dt": pub_date,
            })
    else:
        # RSS 2.0
        channel = root.find("channel")
        if channel is None:
            channel = root
        items = channel.findall("item")
        for item in items:
            title_el = item.find("title")
            title = title_el.text.strip() if title_el is not None and title_el.text else "No title"

            link_el = item.find("link")
            link = link_el.text.strip() if link_el is not None and link_el.text else ""

            desc_el = item.find("description")
            summary = ""
            if desc_el is not None and desc_el.text:
                summary = desc_el.text.strip()[:300]

            date_el = item.find("pubDate")
            pub_date = parse_date(date_el.text if date_el is not None and date_el.text else None)

            articles.append({
                "title": title,
                "link": link,
                "summary": summary,
                "published": pub_date.isoformat() if pub_date else None,
                "published_dt": pub_date,
            })

    return articles


def scan_feeds() -> dict:
    """扫描所有 feed，返回最近 24h 的新文章"""
    since = datetime.now(timezone.utc) - timedelta(hours=HOURS_BACK)
    results = {}

    for name, config in FEEDS.items():
        try:
            xml_bytes = fetch_url(config["url"])
            if not xml_bytes:
                results[name] = {"error": "empty response", "domain": config["domain"]}
                continue

            all_articles = parse_feed(xml_bytes, name)
            if all_articles and "error" in all_articles[0]:
                results[name] = {"error": all_articles[0]["error"], "domain": config["domain"]}
                continue

            new_articles = []
            for article in all_articles:
                pub_dt = article.pop("published_dt", None)
                if pub_dt and pub_dt >= since:
                    new_articles.append(article)

            if new_articles:
                results[name] = {
                    "articles": new_articles,
                    "domain": config["domain"],
                    "count": len(new_articles),
                }
        except subprocess.TimeoutExpired:
            results[name] = {"error": "timeout", "domain": config["domain"]}
        except Exception as e:
            results[name] = {"error": str(e), "domain": config["domain"]}

    return results


def save_digest(results: dict) -> str:
    """保存扫描结果"""
    os.makedirs(DB_PATH, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    filepath = os.path.join(DB_PATH, f"{today}.json")

    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            existing = json.load(f)
        existing.update(results)
        results = existing

    with open(filepath, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    return filepath


def main():
    print(f"🔍 Dreamer RSS Scanner v2 — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"   Scanning {len(FEEDS)} feeds for last {HOURS_BACK}h articles...\n")

    results = scan_feeds()
    filepath = save_digest(results)

    total = 0
    errors = 0
    for name, data in results.items():
        if "error" in data:
            print(f"   ❌ {name}: {data['error']}")
            errors += 1
        elif "articles" in data:
            print(f"   ✅ {name} ({data['domain']}): {data['count']} new")
            for a in data["articles"]:
                print(f"      • {a['title'][:80]}")
            total += data["count"]

    print(f"\n📊 Total: {total} new articles, {errors} errors")
    print(f"📁 Saved to: {filepath}")

    # JSON output for downstream consumption
    print("\n--- JSON OUTPUT ---")
    print(json.dumps(results, ensure_ascii=False))


if __name__ == "__main__":
    main()
