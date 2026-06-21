import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    subconscious = json.load(f)

initial_strength = 5.0

new_entries = [
    {
        'id': 'insight-181-1',
        'content': '好奇心校准作为散步前置步骤：区分真惊喜与三种假惊喜。Dreamer单Agent版CERMIC=历史连接模式加外部锚点双通道噪声滤波。',
        'type': 'insight',
        'strength': initial_strength,
        'connections': ['evolved-rules', 'walk-nutritional-density', 'cognitive-friction', 'mixed-strategy-walking'],
        'created': now,
        'source': 'walk-181',
        'decayed_at': [],
        'quality_score': 8.3
    },
    {
        'id': 'insight-181-2',
        'content': '认知预算最优分配：给定噪声比例，每次散步应在探索/巩固之间动态分配budget。固定3:1比例是保守的噪声滤波策略。',
        'type': 'insight',
        'strength': initial_strength,
        'connections': ['cognitive-budget', 'mixed-strategy-walking', 'curiosity-trap'],
        'created': now,
        'source': 'walk-181',
        'decayed_at': [],
        'quality_score': 8.3
    }
]

subconscious.extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(subconscious, f, indent=2, ensure_ascii=False)

print('Done. Total entries:', len(subconscious))
