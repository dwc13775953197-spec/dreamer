#!/usr/bin/env python3
"""
subconscious_maintain.py — 统一的 subconscious.json 维护脚本

供 DORMANT 和脉冲触发调用。所有对 subconscious.json 的修改都通过此脚本。

用法：
  # 突触缩放（DORMANT 第二阶段）
  python3 subconscious_maintain.py decay [--factor 0.88] [--protect-high] [--protect-low]
  
  # 添加新 insight
  python3 subconscious_maintain.py add --id ins-XXX --type insight --content "文本" --strength 5.0 --score 0.7 --source walk-XXX
  
  # 标记休眠
  python3 subconscious_maintain.py dormancy
  
  # 重激活
  python3 subconscious_maintain.py resurrect --id ins-XXX
  
  # 脚手架维护（从旧 walk 日志复活概念）
  python3 subconscious_maintain.py scaffold --walks-dir ~/hermes_dreamer/walks
  
  # 统计
  python3 subconscious_maintain.py stats

设计原则：
  - 所有 entry 必须有 id, type, content, strength, score, status, created, source, resurrected_count
  - status: active | dormant（不再使用 decayed）
  - strength 不会为负，最低 0
  - decay 是非均匀的：高质量衰减慢，低质量衰减快
"""

import argparse
import json
import random
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

SUB_CONSCIOUS = Path.home() / "hermes_dreamer" / "subconscious.json"
WALKS_DIR = Path.home() / "hermes_dreamer" / "walks"
tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()


def load():
    with open(SUB_CONSCIOUS) as f:
        data = json.load(f)
    if isinstance(data, dict) and "entries" in data:
        return data["entries"]
    return data


def save(entries):
    with open(SUB_CONSCIOUS, "w") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)


def ensure_fields(entry):
    """确保 entry 有所有必要字段"""
    defaults = {
        "strength": 3.0,
        "status": "active",
        "resurrected_count": 0,
        "score": 0.0,
        "decay_speed": 0.5,
        "refs": [],
        "note": "",
    }
    for k, v in defaults.items():
        if k not in entry:
            entry[k] = v
    return entry


def cmd_decay(args):
    """非均匀突触缩放"""
    entries = load()
    factor = args.factor if args.factor else random.uniform(0.85, 0.92)
    
    stats = {"total": len(entries), "protected": 0, "accelerated": 0, "hub_protected": 0}
    
    # 计算入度（被引用次数）
    ref_count: dict[str, int] = {}
    for e in entries:
        for ref in e.get("refs", []):
            ref_count[ref] = ref_count.get(ref, 0) + 1
    
    for entry in entries:
        ensure_fields(entry)
        
        # 基础衰减系数
        decay_f = factor
        
        # 枢纽保护（被 ≥3 条目引用）
        my_refs = ref_count.get(entry.get("id", ""), 0)
        if my_refs >= 3:
            decay_f *= 1.5
            stats["hub_protected"] += 1
        
        # 高质量保护 / 低质量加速
        if entry.get("score", 0) >= 0.7:
            decay_f *= 1.2
            stats["protected"] += 1
        elif entry.get("score", 0) < 0.4:
            decay_f *= 0.8
            stats["accelerated"] += 1
        
        # 应用衰减
        entry["strength"] = round(entry["strength"] * decay_f, 1)
        
        # strength 下限保护
        if entry.get("score", 0) >= 0.7 and entry["strength"] < 2.0:
            entry["strength"] = 2.0
        
        # 休眠标记
        if entry["strength"] < 1.0 and entry.get("score", 0) < 0.4:
            entry["status"] = "dormant"
        elif entry["status"] == "dormant" and entry["strength"] >= 1.0:
            entry["status"] = "active"
    
    save(entries)
    print(f"突触缩放完成: factor={factor:.3f}")
    print(f"  总计: {stats['total']}, 高质量保护: {stats['protected']}, 低质量加速: {stats['accelerated']}, 枢纽保护: {stats['hub_protected']}")
    
    active = [e for e in entries if e["status"] == "active"]
    dormant = [e for e in entries if e["status"] == "dormant"]
    if active:
        strengths = [e["strength"] for e in active]
        print(f"  active: {len(active)}, strength: {min(strengths):.1f}~{max(strengths):.1f}, avg={sum(strengths)/len(strengths):.1f}")
    print(f"  dormant: {len(dormant)}")


def cmd_add(args):
    """添加新 insight"""
    entries = load()
    
    # 检查 id 是否已存在
    existing_ids = {e.get("id") for e in entries}
    if args.id in existing_ids:
        print(f"WARNING: {args.id} 已存在，跳过")
        return
    
    entry = {
        "id": args.id,
        "type": args.type,
        "content": args.content,
        "strength": args.strength,
        "score": args.score,
        "status": "active",
        "created": now,
        "source": args.source or "",
        "resurrected_count": 0,
        "refs": [],
        "note": args.note or "",
    }
    
    entries.append(entry)
    save(entries)
    print(f"✅ 添加 {args.id}: type={args.type}, strength={args.strength}, score={args.score}")


def cmd_dormancy(args):
    """扫描并标记休眠条目"""
    entries = load()
    count = 0
    for entry in entries:
        ensure_fields(entry)
        if entry["strength"] < 1.0 and entry.get("score", 0) < 0.4:
            if entry["status"] != "dormant":
                entry["status"] = "dormant"
                count += 1
        elif entry["status"] == "dormant" and entry["strength"] >= 1.0:
            entry["status"] = "active"
            count += 1
    save(entries)
    print(f"休眠标记: {count} 条变更")


def cmd_resurrect(args):
    """重激活指定条目"""
    entries = load()
    for entry in entries:
        if entry.get("id") == args.id:
            entry["strength"] = 3.0
            entry["status"] = "active"
            entry["resurrected_count"] = entry.get("resurrected_count", 0) + 1
            save(entries)
            print(f"✅ 重激活 {args.id}: strength=3.0")
            return
    print(f"❌ 未找到 {args.id}")


def cmd_scaffold(args):
    """从旧 walk 日志提取概念并检查存活状态"""
    entries = load()
    walks_dir = Path(args.walks_dir) if args.walks_dir else WALKS_DIR
    
    # 获取 7-30 天前的 walk 文件
    walk_files = sorted(walks_dir.glob("*.md"))
    old_walks = []
    for wf in walk_files:
        # 从文件名提取日期
        m = re.search(r"(\d{4}-\d{2}-\d{2})", wf.name)
        if m:
            date_str = m.group(1)
            try:
                walk_date = datetime.strptime(date_str, "%Y-%m-%d")
                days_ago = (datetime.now() - walk_date).days
                if 7 <= days_ago <= 30 and "postmortem" not in wf.name:
                    old_walks.append(wf)
            except:
                pass
    
    if not old_walks:
        print("没有找到 7-30 天前的 walk 日志")
        return
    
    # 随机选 1-2 篇
    selected = random.sample(old_walks, min(2, len(old_walks)))
    
    # 获取现有 entry 的 id 和内容关键词
    existing_ids = {e.get("id") for e in entries}
    existing_contents = {e.get("content", "")[:50] for e in entries}
    
    resurrected = 0
    for wf in selected:
        try:
            content = wf.read_text()
            # 提取核心概念（从 ## 散步 或 ## 洞察 部分）
            concepts = re.findall(r'\*\*(.+?)\*\*', content)
            if not concepts:
                concepts = re.findall(r'## 洞察\n\n(\d+\.\s+.+)', content)
            
            for concept in concepts[:3]:  # 每篇最多 3 个
                concept = concept.strip()
                if len(concept) < 10:
                    continue
                
                # 检查是否已有类似条目
                is_dup = False
                for ec in existing_contents:
                    # 简单重叠检查
                    words1 = set(concept[:50].split())
                    words2 = set(ec[:50].split())
                    if words1 and words2 and len(words1 & words2) / max(len(words1), 1) > 0.5:
                        is_dup = True
                        break
                
                if not is_dup:
                    new_id = f"scaf-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000,9999)}"
                    entry = {
                        "id": new_id,
                        "type": "resurrection",
                        "content": f"从 {wf.stem} 复活的概念: {concept[:200]}",
                        "strength": 2.5,
                        "score": 0.5,
                        "status": "active",
                        "created": now,
                        "source": wf.stem,
                        "resurrected_count": 0,
                        "refs": [wf.stem],
                        "note": f"scaffold resurrection from {wf.name}",
                    }
                    entries.append(entry)
                    resurrected += 1
        except Exception as e:
            print(f"  读取 {wf.name} 失败: {e}")
    
    save(entries)
    print(f"脚手架维护: 检查了 {len(selected)} 篇旧 walk，复活了 {resurrected} 个概念")


def cmd_stats(args):
    """显示统计信息"""
    entries = load()
    active = [e for e in entries if e.get("status") == "active"]
    dormant = [e for e in entries if e.get("status") == "dormant"]
    
    print(f"=== subconscious.json 统计 ===")
    print(f"总计: {len(entries)} (active: {len(active)}, dormant: {len(dormant)})")
    
    if active:
        strengths = [e["strength"] for e in active]
        scores = [e.get("score", 0) for e in active]
        print(f"active strength: {min(strengths):.1f}~{max(strengths):.1f}, avg={sum(strengths)/len(strengths):.1f}")
        print(f"active score: {min(scores):.2f}~{max(scores):.2f}")
    
    # 类型分布
    from collections import Counter
    types = Counter(e.get("type", "?") for e in entries)
    print(f"类型: {dict(types)}")
    
    # 入度分布
    ref_count: dict[str, int] = {}
    for e in entries:
        for ref in e.get("refs", []):
            ref_count[ref] = ref_count.get(ref, 0) + 1
    if ref_count:
        top_refs = sorted(ref_count.items(), key=lambda x: x[1], reverse=True)[:5]
        print(f"高入度节点: {top_refs}")


def main():
    parser = argparse.ArgumentParser(description="subconscious.json 统一维护")
    sub = parser.add_subparsers(dest="command")
    
    # decay
    p_decay = sub.add_parser("decay", help="突触缩放")
    p_decay.add_argument("--factor", type=float, default=None, help="指定衰减系数（默认随机 0.85-0.92）")
    p_decay.add_argument("--protect-high", action="store_true", help="高质量保护")
    p_decay.add_argument("--protect-low", action="store_true", help="低质量加速")
    
    # add
    p_add = sub.add_parser("add", help="添加新条目")
    p_add.add_argument("--id", required=True)
    p_add.add_argument("--type", required=True)
    p_add.add_argument("--content", required=True)
    p_add.add_argument("--strength", type=float, default=3.0)
    p_add.add_argument("--score", type=float, default=0.5)
    p_add.add_argument("--source", default="")
    p_add.add_argument("--note", default="")
    
    # dormancy
    sub.add_parser("dormancy", help="扫描并标记休眠")
    
    # resurrect
    p_res = sub.add_parser("resurrect", help="重激活")
    p_res.add_argument("--id", required=True)
    
    # scaffold
    p_scaf = sub.add_parser("scaffold", help="脚手架维护")
    p_scaf.add_argument("--walks-dir", default=None)
    
    # stats
    sub.add_parser("stats", help="统计")
    
    args = parser.parse_args()
    
    if args.command == "decay":
        cmd_decay(args)
    elif args.command == "add":
        cmd_add(args)
    elif args.command == "dormancy":
        cmd_dormancy(args)
    elif args.command == "resurrect":
        cmd_resurrect(args)
    elif args.command == "scaffold":
        cmd_scaffold(args)
    elif args.command == "stats":
        cmd_stats(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
