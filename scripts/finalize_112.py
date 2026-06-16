import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

new_seeds = [
    {
        'id': 'seed-324',
        'topic': '翻译层作为 DORMANT 新子流程：将梦境隐喻转化为散步可执行的工程决策',
        'source': 'internal-digestion-07',
        'trigger': '园丁梦境早于 walk-112 两天看到同样的问题但未被读取',
        'intensity': 0.6,
        'type': 'research',
        'status': 'pending',
        'created': now,
        'decay_rate': 1
    },
    {
        'id': 'seed-325',
        'topic': '诊断密度作为散步质量负向指标：超过 50% insight 为自身诊断时标记为诊断过载',
        'source': 'internal-digestion-07',
        'trigger': 'walk-108 到 walk-112 的退化趋势',
        'intensity': 0.55,
        'type': 'research',
        'status': 'pending',
        'created': now,
        'decay_rate': 1
    },
    {
        'id': 'seed-326',
        'topic': '结构性修复作为 evolved_rules 新分类：区分诊断性规则和结构性规则',
        'source': 'internal-digestion-07',
        'trigger': '50 条 evolved_rules 中仅 ~20% 为结构性规则',
        'intensity': 0.5,
        'type': 'research',
        'status': 'pending',
        'created': now,
        'decay_rate': 1
    }
]

soul['interest_queue'].extend(new_seeds)

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print('Added 3 internal digestion seeds, total queue: {}'.format(len(soul['interest_queue'])))
