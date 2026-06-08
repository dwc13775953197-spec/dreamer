# Blogwatcher × Dreamer 集成方案

## 架构

```
┌─────────────────────────────────────────────────┐
│                  Dreamer 散步流程                  │
│                                                   │
│  步骤 2.x: 外部信息扫描（新增）                      │
│  ┌─────────────────────────────────────────────┐  │
│  │ 2.7 RSS 扫描                                 │  │
│  │  - blogwatcher-cli scan（代理环境）           │  │
│  │  - 获取最近 24h 新文章                        │  │
│  │  - 筛选与当前话题相关的文章                    │  │
│  │  - 提取标题+摘要作为散步素材                   │  │
│  └─────────────────────────────────────────────┘  │
│                      ↓                             │
│  步骤 3-7: 正常散步流程（RSS 素材作为输入）          │
│                      ↓                             │
│  步骤 8: 叙事完整性检查（RSS 文章作为新材料源）       │
└─────────────────────────────────────────────────┘
```

## 已订阅源

| 博客 | URL | 领域 |
|------|-----|------|
| Karpathy Blog | https://karpathy.ai | AI/ML 核心 |
| LessWrong | https://lesswrong.com | 理性/认知/AI 安全 |
| Import AI | https://importai.substack.com | AI 研究周报 |
| The Gradient | https://thegradient.pub | ML 研究深度 |
| Weird ML | https://weirdml.substack.com | 前沿 ML 怪东西 |

## 集成点

### 1. 散步流程（SKILL.md 步骤 2.7）

在现有步骤 2.6（查询 Obsidian wiki）之后新增：

```
2.7 扫描 RSS 新文章：
  - 执行: blogwatcher-cli --db ~/hermes_dreamer/blogwatcher.db articles
  - 筛选最近 24h 内的未读文章
  - 如果当前散步话题明确 → 筛选相关文章
  - 如果自由散步 → 取最新 3 篇作为素材
  - 提取标题 + 前 200 字摘要
  - 标记为已读: blogwatcher-cli read <id>
```

### 2. 脉冲 Cron（新增独立 Cron）

**Cron 4: RSS 定时扫描（每 6 小时）**
```
schedule: every 6h
deliver: local（不推 Discord，只更新数据库）

任务：
1. blogwatcher-cli scan（走代理）
2. 如果有新文章 → 写入 ~/hermes_dreamer/rss-digest/YYYY-MM-DD.md
3. 更新 soul.json 的 last_rss_scan 时间戳
```

### 3. 晨间对话 Cron（增强）

在现有晨间对话步骤中加一步：
```
读取 ~/hermes_dreamer/rss-digest/ 最新文件
如果有未分享的有趣文章 → 在晨间对话中提及
```

### 4. 周复盘 Cron（增强）

在现有周复盘步骤中加一步：
```
统计本周 RSS 扫描到的文章数
筛选被散步引用过的文章
写入周复盘报告："本周从 RSS 获取 X 篇文章，其中 Y 篇被散步引用"
```

## 网络方案

blogwatcher-cli 的 Go HTTP 客户端不读 shell 环境变量代理，且 Python urllib 不支持 socks5。
最终方案：**curl + socks5 代理**。

- 代理地址：`socks5://192.168.188.3:4781`（已验证可用）
- HTTP 代理 4780 也可用，但 Python urllib 连接较慢，暂不采用
- Go 的 blogwatcher-cli 因私有地址限制无法直接使用代理

```python
# ~/hermes_dreamer/scripts/rss_scan.py
import feedparser, json, os, urllib.request
from datetime import datetime, timedelta

PROXY = "http://192.168.188.3:4781"
FEEDS = {
    "karpathy": "https://karpathy.ai/rss.xml",
    "lesswrong": "https://lesswrong.com/feed.xml",
    "importai": "https://importai.substack.com/feed",
    "thegradient": "https://thegradient.pub/rss/",
    "weirdml": "https://weirdml.substack.com/feed",
}

proxy_handler = urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})
opener = urllib.request.build_opener(proxy_handler)

results = {}
since = datetime.now() - timedelta(hours=24)

for name, url in FEEDS.items():
    try:
        resp = opener.open(url, timeout=15)
        feed = feedparser.parse(resp.read())
        new_articles = []
        for entry in feed.entries[:10]:
            published = entry.get("published_parsed") or entry.get("updated_parsed")
            if published:
                pub_dt = datetime(*published[:6])
                if pub_dt > since:
                    new_articles.append({
                        "title": entry.title,
                        "link": entry.link,
                        "summary": entry.get("summary", "")[:300],
                        "published": pub_dt.isoformat(),
                    })
        if new_articles:
            results[name] = new_articles
    except Exception as e:
        results[name] = {"error": str(e)}

# 写入 digest
digest_dir = os.path.expanduser("~/hermes_dreamer/rss-digest")
os.makedirs(digest_dir, exist_ok=True)
today = datetime.now().strftime("%Y-%m-%d")
with open(f"{digest_dir}/{today}.json", "w") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

# 输出摘要
total = sum(len(v) for v in results.values() if isinstance(v, list))
print(f"Scanned {len(FEEDS)} feeds, {total} new articles in last 24h")
for name, articles in results.items():
    if isinstance(articles, list):
        for a in articles:
            print(f"  [{name}] {a['title']}")
    else:
        print(f"  [{name}] ERROR: {articles['error']}")
```

### 方案 B：CDP 浏览器（web-access skill）

用浏览器自动化访问 RSS URL，适合 feedparser 解析不了的站点。

## Cron 配置

### Cron 4: RSS 扫描（新增）

```yaml
name: Dreamer RSS 扫描
schedule: every 6h
deliver: local
enabled_toolsets: [terminal]
prompt: |
  你是 Dreamer。执行 RSS 扫描任务。
  
  1. 运行 Python 脚本扫描 RSS：
     python3 ~/hermes_dreamer/scripts/rss_scan.py
  
  2. 如果扫描到新文章：
     a. 读取 ~/hermes_dreamer/rss-digest/YYYY-MM-DD.json
     b. 筛选与当前兴趣队列相关的文章
     c. 将相关文章摘要写入散步素材文件
     d. 更新 soul.json 的 last_rss_scan
  
  3. 如果没有新文章 → 安静离开
  
  4. 写审计日志到 audit.jsonl
```

## 文件结构

```
~/hermes_dreamer/
├── blogwatcher.db              # blogwatcher SQLite（备用）
├── rss-digest/                 # RSS 扫描结果
│   ├── 2026-06-02.json
│   └── ...
├── scripts/
│   └── rss_scan.py             # Python RSS 扫描器
└── wiki/
    └── raw/
        └── rss/                # RSS 文章存档
            └── YYYY-MM-DD--<slug>.md
```

## 与 llm-wiki 的关系

RSS 文章作为外部素材流入 Dreamer 的散步流程。
高质量的文章摘要可以存入 Dreamer wiki 的 raw/rss/ 目录，
作为散步的参考材料（类似 raw/articles/ 的作用）。

## 优先级

1. **先实现方案 A**（Python RSS 扫描器）— 不依赖 blogwatcher-cli 网络
2. **再配置 Cron 4** — 每 6 小时自动扫描
3. **最后更新 SKILL.md** — 散步流程步骤 2.7
4. **最后增强晨间对话和周复盘** — RSS 素材分享
