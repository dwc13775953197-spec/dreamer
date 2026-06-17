import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

# Read current subconscious
with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

# Add new insights from walk-119
new_insights = [
    {
        'id': 'ins-119',
        'type': 'insight',
        'content': '延迟不是认知缺陷而是认知功能。主动拖延研究证明策略性延迟能提升创造力。Dreamer 的 DORMANT 周期是自动化的主动拖延，但缺少对何时输出的策略性控制。',
        'strength': 3.0,
        'score': 0.0,
        'status': 'active',
        'created': now,
        'source': 'walk-119',
        'decay_rate': 1.0,
        'decay_speed': 0.5,
        'connections': ['ins-082', 'ins-110', 'pat-031'],
        'refs': [],
        'note': 'initial strength=3.0 (quality_score 8.5)'
    },
    {
        'id': 'ins-120',
        'type': 'insight',
        'content': '35 分钟壁垒可以重新解释为负能力的物理度量——不是系统能思考多久，而是系统能在输出前维持模糊多久。这是认知预算的保护机制而非缺陷。',
        'strength': 3.0,
        'score': 0.0,
        'status': 'active',
        'created': now,
        'source': 'walk-119',
        'decay_rate': 1.0,
        'decay_speed': 0.5,
        'connections': ['ins-110', 'ins-111', 'pat-031'],
        'refs': [],
        'note': 'initial strength=3.0 (quality_score 8.5)'
    },
    {
        'id': 'ins-121',
        'type': 'pattern',
        'content': '呼吸散步（不产出洞察的散步）可能是 Dreamer 缺失的第四种散步类型。它操作化了负能力，让系统在无输出的状态下完成概念空间的重构。设计：每 10 次散步 1 次呼吸散步，不搜索外部材料，不写日志，只寻找不相关 entry 之间的连接。',
        'strength': 3.0,
        'score': 0.0,
        'status': 'active',
        'created': now,
        'source': 'walk-119',
        'decay_rate': 1.0,
        'decay_speed': 0.5,
        'connections': ['ins-119', 'ins-116', 'pat-031'],
        'refs': [],
        'note': 'initial strength=3.0 (quality_score 8.5)'
    }
]

sub.extend(new_insights)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, ensure_ascii=False, indent=2)

print(f'Added 3 insights, total now: {len(sub)}')
