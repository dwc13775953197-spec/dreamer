#!/usr/bin/env python3
import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    data = json.load(f)

entries = data if isinstance(data, list) else data.get('entries', [])

new_insights = [
    {
        'id': 'insight-212-1',
        'type': 'insight',
        'status': 'active',
        'content': '遗忘-锁死双螺旋：Dreamer 的衰减机制需要同时完成两个任务——遗忘不该留的低价值知识 + 解锁该忘的高连接病理性 hub。当前衰减只做了第一件事（且不彻底），第二件事完全缺失。',
        'strength': 5.0,
        'connections': ['seed-211-2', 'seed-210-1', 'walk-211'],
        'created': now.isoformat(),
        'decay_rate': 0.05,
        'source': 'walk-212'
    },
    {
        'id': 'insight-212-2',
        'type': 'insight',
        'status': 'active',
        'content': '建设性遗忘的三机制设计：连接衰减（遗忘）、反向审计（识别锁死）、正向重激活（防止丢失）。Walk 211 做了第3点，第1、2点完全没有机制支持。',
        'strength': 5.0,
        'connections': ['insight-212-1', 'seed-211-3'],
        'created': now.isoformat(),
        'decay_rate': 0.05,
        'source': 'walk-212'
    },
    {
        'id': 'insight-212-3',
        'type': 'insight',
        'status': 'active',
        'content': '引用连带衰减模型：connections 权重应该是源 entry strength 的函数。当源 entry strength 衰减时，其出链的引用价值同步降低，实现连带衰减，打破病理性 hub 的结构性锁死。',
        'strength': 5.0,
        'connections': ['insight-212-1', 'seed-211-1'],
        'created': now.isoformat(),
        'decay_rate': 0.05,
        'source': 'walk-212'
    }
]

entries.extend(new_insights)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'Added 3 insights. Total entries: {len(entries)}')
