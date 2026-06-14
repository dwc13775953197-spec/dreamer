#!/usr/bin/env python3
"""
subconscious_repair.py — 修复 subconscious.json 数据结构

修复内容：
1. 统一 status 字段：decayed → dormant（新格式）
2. 修复负 strength：clamp 到 0
3. 添加缺失字段：resurrected_count, status
4. 清理无效条目（strength <= 0 且 score <= 0 的 decayed 条目）
5. 为每个 entry 确保有所有必要字段

用法：
  python3 ~/hermes_dreamer/scripts/subconscious_repair.py
"""

import json
from pathlib import Path

SUB_CONSCIOUS = Path.home() / "hermes_dreamer" / "subconscious.json"

def repair():
    with open(SUB_CONSCIOUS) as f:
        data = json.load(f)
    
    # 确保是 list
    if isinstance(data, dict) and "entries" in data:
        entries = data["entries"]
    elif isinstance(data, list):
        entries = data
    else:
        print(f"ERROR: unexpected format {type(data)}")
        return
    
    print(f"修复前: {len(entries)} 条")
    
    fixed = []
    removed = 0
    
    for entry in entries:
        # 确保必要字段存在
        if "status" not in entry:
            entry["status"] = "active"
        if "resurrected_count" not in entry:
            entry["resurrected_count"] = 0
        if "score" not in entry:
            entry["score"] = 0.0
        
        # 修复 status 值
        if entry["status"] == "decayed":
            entry["status"] = "dormant"
        elif entry["status"] == "" or entry["status"] is None:
            entry["status"] = "active"
        
        # 修复负 strength
        if entry["strength"] < 0:
            print(f"  修复 {entry.get('id','?')}: strength {entry['strength']} → 0.0")
            entry["strength"] = 0.0
        
        # 清理无效条目：strength=0 且 score=0 且 status=dormant
        if entry["strength"] == 0.0 and entry.get("score", 0) == 0.0 and entry["status"] == "dormant":
            print(f"  移除 {entry.get('id','?')}: strength=0, score=0, dormant")
            removed += 1
            continue
        
        fixed.append(entry)
    
    print(f"修复后: {len(fixed)} 条 (移除 {removed} 条)")
    
    # 统计
    active = [e for e in fixed if e["status"] == "active"]
    dormant = [e for e in fixed if e["status"] == "dormant"]
    print(f"  active: {len(active)}, dormant: {len(dormant)}")
    
    if active:
        strengths = [e["strength"] for e in active]
        print(f"  active strength: min={min(strengths):.2f}, max={max(strengths):.2f}, avg={sum(strengths)/len(strengths):.2f}")
    
    # 写回（保持 list 格式）
    with open(SUB_CONSCIOUS, "w") as f:
        json.dump(fixed, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已写入 {SUB_CONSCIOUS}")

if __name__ == "__main__":
    repair()
