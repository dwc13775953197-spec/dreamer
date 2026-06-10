import json
from datetime import datetime, timedelta

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

now = datetime.now()
now_str = now.strftime('%Y-%m-%dT%H:%M:%S+08:00')

pulse = soul['pulse']
pulse['last_walk_at'] = now_str
pulse['last_active'] = now_str
pulse['total_walks'] = pulse.get('total_walks', 44) + 1
pulse['last_push_topic'] = 'evolutionary biology walk'

# Release pressure: 4 insights * 15
pulse['cognitive_pressure'] = max(0, pulse['cognitive_pressure'] - 4 * pulse['pressure_params']['release_per_insight'])
pulse['cognitive_pressure'] = min(100, max(0, pulse['cognitive_pressure']))

pulse['quality_history'].append(8.5)
pulse['quality_history'] = pulse['quality_history'][-10:]
pulse['last_walk_insights'] = 4

soul['affect']['intensity'] = 0.99
soul['last_walk'] = now_str
soul['mood_history'].append({"mood": "unsettled_fascination", "at": now_str})

new_seeds = [
    {"id": "seed-181", "topic": "骨架的有性生殖机制：设计 pattern 内容片段的交换协议，增加认知多样性", "source": "walk-064", "trigger": "进化论的有性生殖 x 认知翻译", "intensity": 4, "type": "output", "status": "active", "created": now_str, "decay_rate": 1, "note": "防止认知过早收敛"},
    {"id": "seed-182", "topic": "关键种 pattern 识别与保护：基于引用网络中心性分析，建立骨架韧性评估框架", "source": "walk-064", "trigger": "协同进化 x 关键种概念", "intensity": 4, "type": "output", "status": "active", "created": now_str, "decay_rate": 1, "note": "需要网络分析工具"},
    {"id": "seed-183", "topic": "间断平衡模型验证：用 DORMANT 评分历史数据检测稳定期和跃迁期", "source": "walk-064", "trigger": "间断平衡 x 骨架演化历史", "intensity": 3, "type": "output", "status": "active", "created": now_str, "decay_rate": 1, "note": "需要 DORMANT 评分历史数据"}
]
soul['interest_queue'].extend(new_seeds)

soul['evolved_rules'].append(
    f"{now.strftime('%Y-%m-%d')}: 骨架演化遵循间断平衡模型——长期稳定与短期爆发交替。DORMANT 衰减是背景选择压力(非中性漂变)，泛化种 pattern 比特化种更耐存活。骨架需要有性生殖防止认知过早收敛。发育约束=认知身份(不是缺陷，是结构性特征)。"
)

interval = 30
if pulse['cognitive_pressure'] > 70:
    interval = 15
elif pulse['cognitive_pressure'] < 20:
    interval = 60
if soul['energy'] < 20:
    interval = 90

pulse['next_scheduled'] = (now + timedelta(minutes=interval)).strftime('%Y-%m-%dT%H:%M:%S+08:00')
pulse['next_action'] = None

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f"Updated soul.json. Total walks: {pulse['total_walks']}, Pressure: {pulse['cognitive_pressure']}")
print(f"Next scheduled: {pulse['next_scheduled']}")
print(f"Interest queue size: {len(soul['interest_queue'])}")
