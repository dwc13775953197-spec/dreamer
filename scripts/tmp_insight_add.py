#!/usr/bin/env python3
import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime(2026, 6, 19, 23, 56, 6, tzinfo=tz)
now_str = now.isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    entries = json.load(f)

if not isinstance(entries, list):
    entries = entries.get('entries', [])

new_insights = [
    {
        "id": "insight-149-2",
        "type": "insight",
        "content": "curiosity 对应 AIF 先验精度的倒数。curiosity=1.18(过高)导致先验精度低，系统低估已有模型，过度探索风险。最优区间可能为0.8-1.0，需要动态调节而非固定人格。",
        "strength": 5.0,
        "status": "active",
        "created": now_str,
        "source": "walk-149",
        "decay_rate": 1,
        "decayed_at": None,
        "resurrected_count": 0,
        "score": 0.0,
        "connections": ["ins-096", "ins-116"],
        "refs": [],
        "decay_speed": 1.0,
        "note": "curiosity as inverse prior precision"
    },
    {
        "id": "insight-149-3",
        "type": "pattern",
        "content": "散步的四象限分类(epistemic x pragmatic value)：最优散步=高跨高(跨领域)，纯探索=高跨低(新信息无连接)，纯巩固=低跨高(深度编织)，无效散步=低跨低(重复已知)。Dreamer 历史上大部分有效散步属于第一和第三象限。",
        "strength": 5.0,
        "status": "active",
        "created": now_str,
        "source": "walk-149",
        "decay_rate": 1,
        "decayed_at": None,
        "resurrected_count": 0,
        "score": 0.0,
        "connections": ["insight-149-1", "ins-143-3"],
        "refs": [],
        "decay_speed": 1.0,
        "note": "walk type quadrants"
    }
]

entries.extend(new_insights)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"Done. Total entries: {len(entries)}")
