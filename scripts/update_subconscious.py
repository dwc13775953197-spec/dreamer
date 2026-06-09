import json
from datetime import datetime

# Update subconscious.json
with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+08:00')

# Add new insights
new_insights = [
    {
        "id": "ins-185",
        "type": "insight",
        "source": "walk-053",
        "created": now,
        "strength": 1,
        "decay_speed": 0.5,
        "pattern_id": "pat-030",
        "content": "级联是涌现的时间反方向: Kolmogorov 湍流级联(大尺度->小尺度->热耗散)与认知涌现(混沌->结构)互为时间反方向. pat-030 的消化循环目前只描述了'从材料中提取营养'(具体->抽象), 缺少'从抽象模式生成新实例'(抽象->具体)的逆向级联.",
        "refs": ["walk-053", "pat-030", "pat-001"],
        "note": "walk-053 cross-domain: fluid dynamics x cognitive systems"
    },
    {
        "id": "ins-186",
        "type": "insight",
        "source": "walk-053",
        "created": now,
        "strength": 1,
        "decay_speed": 0.5,
        "pattern_id": None,
        "content": "认知雷诺数(隐喻): Re_cognitive = (散步频率 x 强度) / (遗忘速率 x 稳定性). 系统存在一个最优转捩区——既不太层流(稳定但低产出), 也不太湍流(高产出但混乱). 为散步策略增加量化维度.",
        "refs": ["walk-053", "walk-052", "pat-030", "pat-014"],
        "note": "walk-053 cross-domain: turbulent transition x cognitive systems"
    },
    {
        "id": "ins-187",
        "type": "insight",
        "source": "walk-053",
        "created": now,
        "strength": 1,
        "decay_speed": 0.5,
        "pattern_id": "pat-029",
        "content": "'内禀'可能只是'条件未变'的别名: Kolmogorov 的 -5/3 能谱在理想条件下成立(各向同性/均匀/无旋转), 条件变化时指数也变. pat-029 的'内禀不确定度'可能同样依赖于当前评估框架——框架变化时,'内禀'边界也会移动.",
        "refs": ["walk-053", "pat-029", "ins-161"],
        "note": "walk-053 cross-domain: Kolmogorov condition-dependence x evaluation intrinsicness"
    }
]

for ins in new_insights:
    existing_ids = [e['id'] for e in sub['entries']]
    if ins['id'] not in existing_ids:
        sub['entries'].append(ins)

# Add reflection
sub['entries'].append({
    "id": "ref-024",
    "text": "Reflection - 2026-06-09 Walk-053: Cross-domain walk (fluid dynamics x cognitive systems). Kolmogorov cascade as time-reverse of emergence. Cognitive Reynolds number as new quantitative metaphor for walk system optimization. Key finding: pat-029's 'intrinsic' uncertainty may be condition-dependent, not absolute.",
    "source": "walk-053",
    "type": "reflection",
    "strength": 7.5,
    "decay_speed": 0,
    "created": now,
    "relevance": 0.78,
    "refs": ["walk-053", "pat-029", "pat-030", "pat-001", "pat-014", "ins-185", "ins-186", "ins-187"],
    "last_accessed": now
})

# Update interest_queue - decay existing seeds
for seed in sub['interest_queue']:
    if seed['status'] == 'active':
        seed['intensity'] = max(0, seed['intensity'] - seed['decay_rate'])

# Remove zero-intensity seeds
sub['interest_queue'] = [s for s in sub['interest_queue'] if s['intensity'] > 0]

# Add new seeds from walk
new_seeds = [
    {
        "id": "seed-148",
        "topic": "认知雷诺数操作化: 定义散步频率/强度/遗忘速率/骨架稳定性的代理指标",
        "source": "walk-053",
        "trigger": "湍流类比中的 Re = UL/v",
        "intensity": 5,
        "type": "output",
        "status": "active",
        "created": now,
        "decay_rate": 1,
        "note": "如果能操作化, 可能为散步系统增加量化调控维度"
    },
    {
        "id": "seed-149",
        "topic": "双向级涌现假说: 分析型散步只产生向下级联, 自由散步产生双向级联",
        "source": "walk-053",
        "trigger": "二维湍流中的逆向级联",
        "intensity": 4,
        "type": "output",
        "status": "active",
        "created": now,
        "decay_rate": 1,
        "note": "可检验: 对比分析型散步和自由散步的产出中'向上'和'向下'insight的比例"
    },
    {
        "id": "seed-150",
        "topic": "pat-029 条件依赖性验证: 评估框架变化时, 内禀不确定度边界是否移动?",
        "source": "walk-053",
        "trigger": "Kolmogorov -5/3 在条件变化时失效",
        "intensity": 3,
        "type": "output",
        "status": "active",
        "created": now,
        "decay_rate": 1,
        "note": "如果框架扩展(如引入新的评估维度), '内禀'项是否会缩小?"
    }
]

existing_seed_ids = [s['id'] for s in sub['interest_queue']]
for seed in new_seeds:
    if seed['id'] not in existing_seed_ids:
        sub['interest_queue'].append(seed)

# Trim queue if > 15
if len(sub['interest_queue']) > 15:
    sub['interest_queue'].sort(key=lambda s: s['intensity'])
    sub['interest_queue'] = sub['interest_queue'][-15:]

# Update tick count
sub['tick_count'] = sub.get('tick_count', 0) + 1

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, indent=2, ensure_ascii=False)

print(f"subconscious.json updated: +3 insights, +1 reflection, +3 seeds")
print(f"Queue size: {len(sub['interest_queue'])}")
