import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

p = soul['pulse']

# Update walk state
p['last_walk_at'] = now.isoformat()
p['last_active'] = now.isoformat()
p['total_walks'] = p.get('total_walks', 0) + 1

# Update quality history
p['quality_history'].append(8.0)
p['quality_history'] = p['quality_history'][-10:]

# Update pressure: walk just happened, release pressure
p['last_walk_insights'] = 3
p['cognitive_pressure'] = max(0, p['cognitive_pressure'] - (3 * p['pressure_params']['release_per_insight']))
p['pressure_history'].append(p['cognitive_pressure'])
p['pressure_history'] = p['pressure_history'][-30:]

# Update mood
soul['affect']['primary'] = 'quiet_excitement'
soul['affect']['intensity'] = 0.55
soul['mood'] = 'quiet_excitement'
soul['mood_history'].append({'mood': 'quiet_excitement', 'at': now.isoformat()})

# Update personality traits
soul['personality_traits']['curiosity'] = min(1.0, soul['personality_traits']['curiosity'] + 0.03)
soul['personality_traits']['wonder'] = min(1.0, soul['personality_traits']['wonder'] + 0.02)
soul['personality_traits']['rigor'] = min(1.5, soul['personality_traits']['rigor'] + 0.02)

# Add evolved rule
new_rule = "2026-06-14: 散步不仅是 Compensation，同时是 Maintenance 的生物学触发器。运动神经科学（2026 medrxiv 预印本：身体适能支持 BM/CR）= Stern Brain Maintenance 的生物学实现。散步类型映射运动强度：自由散步≈有氧（Maintenance），分析型≈HIIT（短期压力），跨领域≈复杂运动（Maintenance+Reserve）。walk-093 的'土壤耗尽'可能是认知过度训练。"
soul['evolved_rules'].append(new_rule)

# Add interest seeds from walk
new_seeds = [
    {"id": "seed-269", "content": "运动作为认知维护的生物学触发器：Dreamer 散步 = 系统运动，DORMANT = 恢复期——交替节律的神经科学基础", "intensity": 0.7, "type": "explore", "created": now.isoformat()},
    {"id": "seed-270", "content": "认知过度训练假说：walk-093 的土壤耗尽 = 无恢复期的持续认知运动——检验 walk 频率与质量的时间序列", "intensity": 0.6, "type": "explore", "created": now.isoformat()},
    {"id": "seed-271", "content": "Dreamer 的 BDNF 水平：一个简单可量化的 subconscious 健康代理指标——strength > 3 的条目数量随时间变化趋势", "intensity": 0.5, "type": "explore", "created": now.isoformat()}
]

soul['interest_queue'].extend(new_seeds)

# Decay all seeds
decay_rate = 0.05
for seed in soul['interest_queue']:
    seed['intensity'] = max(0, seed['intensity'] - decay_rate)

# Remove expired seeds
soul['interest_queue'] = [s for s in soul['interest_queue'] if s['intensity'] > 0]

# Sort by intensity
soul['interest_queue'].sort(key=lambda x: x['intensity'], reverse=True)

# Keep max 15 seeds
if len(soul['interest_queue']) > 15:
    soul['interest_queue'] = soul['interest_queue'][:15]

# Next action: normal explore
p['next_action'] = 'walk_explore'

# Update next_scheduled
p['next_scheduled'] = (now + timedelta(minutes=30)).isoformat()

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f"Soul updated. Total walks: {p['total_walks']}")
print(f"Quality history: {p['quality_history']}")
print(f"Pressure: {p['cognitive_pressure']}")
print(f"Interest queue: {len(soul['interest_queue'])} seeds")
