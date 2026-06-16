import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    data = json.load(f)

quality_score = 8.5
initial_strength = 5.0  # quality >= 8.0

new_entries = [
    {
        'id': 'ins-076',
        'type': 'pattern',
        'content': 'Dreamer DORMANT 是衰减引擎不是巩固引擎：缺少 Importance 筛选（散步的结构化输出）、Merge 策略（实体解析）、双维度衰减（结构性+情境性）、Eviction（骨架主动淘汰）。当前只覆盖 Decay 的一个子集（均匀衰减）。',
        'strength': initial_strength,
        'status': 'active',
        'created': now,
        'source': 'walk-112',
        'decay_rate': 1.0,
        'connections': ['pat-011', 'pat-014', 'pat-030'],
        'decayed_at': None,
        'resurrected_count': 0,
        'score': 0.0,
        'refs': [],
        'decay_speed': 0.5,
        'note': 'Hindsight 2026 四杠杆框架映射'
    },
    {
        'id': 'ins-077',
        'type': 'insight',
        'content': '成功陷阱的结构性根源是 Importance 筛选缺失。当所有产出被平等对待时，高产但低结构变化的散步产生大量看起来重要但不改变骨架的 insight，消耗注意力但不提供认知杠杆。',
        'strength': initial_strength,
        'status': 'active',
        'created': now,
        'source': 'walk-112',
        'decay_rate': 1.0,
        'connections': ['ins-076', 'pat-014'],
        'decayed_at': None,
        'resurrected_count': 0,
        'score': 0.0,
        'refs': [],
        'decay_speed': 0.5,
        'note': ''
    },
    {
        'id': 'ins-078',
        'type': 'insight',
        'content': '骨架需要认知对象索引来实现 Merge。当前骨架是术语驱动的——同一认知对象用不同术语会被存储为不同 pattern。pat-011 和 pat-030 讨论同一件事（记忆随时间退化）但从未合并。',
        'strength': initial_strength,
        'status': 'active',
        'created': now,
        'source': 'walk-112',
        'decay_rate': 1.0,
        'connections': ['ins-076', 'pat-011', 'pat-030'],
        'decayed_at': None,
        'resurrected_count': 0,
        'score': 0.0,
        'refs': [],
        'decay_speed': 0.5,
        'note': ''
    },
    {
        'id': 'ins-079',
        'type': 'pattern',
        'content': '双维度衰减（结构性+情境性）比均匀衰减更合理。结构性维度（连接数越多衰减越慢）已被 walk-089 部分解决，情境维度（前提条件是否仍然成立）完全缺失——这是记忆陈旧性检测的核心缺失。',
        'strength': initial_strength,
        'status': 'active',
        'created': now,
        'source': 'walk-112',
        'decay_rate': 1.0,
        'connections': ['ins-066', 'ins-069', 'pat-011'],
        'decayed_at': None,
        'resurrected_count': 0,
        'score': 0.0,
        'refs': [],
        'decay_speed': 0.5,
        'note': 'Hindsight Graphiti 时间戳方案 inspiration'
    }
]

data.extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Added 4 entries to subconscious.json, total now: {}'.format(len(data)))
