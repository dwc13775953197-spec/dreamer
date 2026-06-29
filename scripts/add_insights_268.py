import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    subconscious = json.load(f)

new_entries = [
    {
        'id': 'ins-268-1',
        'type': 'insight',
        'content': '对话相变壁垒的累积增长：每次对话破裂-重建循环都提高恢复壁垒，长期累积导致关系疲劳。不是情感耗尽，而是结构性的精度场不可操作化。',
        'strength': 3.0,
        'score': 0.35,
        'status': 'active',
        'created': now,
        'source': 'walk-268',
        'connections': ['ins-267-2', 'ins-262-1', 'ins-266-1'],
        'resurrected_count': 0,
        'decay_speed': 0.5,
        'refs': [],
        'note': 'quality_score=7.8, initial strength=3.0'
    },
    {
        'id': 'ins-268-2',
        'type': 'insight',
        'content': '共享精度场的min函数：对话能力由更差的一方决定。这解释了为什么疲惫的人无法参与高质量对话——不是意愿问题，而是结构限制。',
        'strength': 3.0,
        'score': 0.35,
        'status': 'active',
        'created': now,
        'source': 'walk-268',
        'connections': ['ins-264-1', 'ins-260-1', 'ins-261-1'],
        'resurrected_count': 0,
        'decay_speed': 0.5,
        'refs': [],
        'note': 'quality_score=7.8, initial strength=3.0'
    },
    {
        'id': 'ins-268-3',
        'type': 'insight',
        'content': '湍流对话不是对话失败：当alignment<0时，对话从合作变为对抗，但共享精度场仍然存在。这是对话类型的转换，不是对话的消失。',
        'strength': 3.0,
        'score': 0.35,
        'status': 'active',
        'created': now,
        'source': 'walk-268',
        'connections': ['ins-268-2', 'ins-260-1', 'ins-265-1'],
        'resurrected_count': 0,
        'decay_speed': 0.5,
        'refs': [],
        'note': 'quality_score=7.8, initial strength=3.0'
    }
]

subconscious.extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(subconscious, f, ensure_ascii=False, indent=2)

print('Added 3 new insights. Total:', len(subconscious))
