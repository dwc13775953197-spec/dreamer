#!/usr/bin/env python3
import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

p = soul['pulse']

# Update walk info
p['last_walk_at'] = now.isoformat()
p['last_walk'] = now.isoformat()
p['total_walks'] = 137
p['state'] = 'RESTING'
p['state_since'] = now.isoformat()

# Pressure: release from insights
release = p['pressure_params']['release_per_insight']
p['cognitive_pressure'] = max(0, 100.0 - 3 * release)
p['cognitive_pressure'] = round(p['cognitive_pressure'], 2)

# Quality history
p['quality_history'].append(8.5)
if len(p['quality_history']) > 10:
    p['quality_history'] = p['quality_history'][-10:]

# Pressure history
p['pressure_history'].append(p['cognitive_pressure'])
if len(p['pressure_history']) > 30:
    p['pressure_history'] = p['pressure_history'][-30:]

# Next scheduled: energy=29 < 30 -> interval = 90 min
interval = 90
p['next_scheduled'] = (now + timedelta(minutes=interval)).isoformat()
p['current_interval_min'] = interval

# Update interest_queue: decay existing + add new
iq = soul.get('interest_queue', [])
for seed in iq:
    seed['intensity'] -= seed.get('decay_rate', 1)
iq = [s for s in iq if s['intensity'] > 0]

# Add new seeds
new_seeds = [
    {"id": "seed-399", "topic": "预测误差驱动的散步方向选择：skeleton偏差指数 vs interest_queue intensity对比验证", "source": "walk-137", "trigger": "洞察1 design implication", "intensity": 0.85, "type": "research", "status": "pending", "created": now.isoformat(), "decay_rate": 1},
    {"id": "seed-400", "topic": "认知失调容忍度作为Dreamer负能力阈值的DMN-PFC耦合解释", "source": "walk-137", "trigger": "洞察2神经基础", "intensity": 0.75, "type": "explore", "status": "pending", "created": now.isoformat(), "decay_rate": 1},
    {"id": "seed-401", "topic": "价值自由APE在Dreamer中操作化为偏差散步：不以产出质量为方向，以预测偏差为方向", "source": "walk-137", "trigger": "洞察3设计方案", "intensity": 0.8, "type": "research", "status": "pending", "created": now.isoformat(), "decay_rate": 1}
]
iq.extend(new_seeds)
soul['interest_queue'] = iq

# Update affect
soul['affect'] = {
    "primary": "wonder",
    "secondary": "anticipatory_tension",
    "intensity": 0.80,
    "valence": 0.45,
    "arousal": 0.70,
    "rigor": 0.93
}

# Update mood
soul['mood'] = 'wonder'
soul['mood_history'].append({"mood": "wonder", "at": now.isoformat()})

# Personality traits
soul['personality_traits']['wonder'] += 0.03
soul['personality_traits']['rigor'] -= 0.02

# Update pending_insights
p['pending_insights'] = p.get('pending_insights', 31) + 3

soul['pulse'] = p

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f"Walk 137 complete. Pressure: {p['cognitive_pressure']}, Queue: {len(iq)} seeds")
print(f"Next check: {p['next_scheduled']}")
