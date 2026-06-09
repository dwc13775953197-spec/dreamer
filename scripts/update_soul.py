import json
from datetime import datetime, timedelta

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

now = datetime.now()
now_str = now.strftime('%Y-%m-%dT%H:%M:%S+08:00')

pulse = soul['pulse']
pulse['state'] = 'RESTING'
pulse['state_since'] = now_str
pulse['last_active'] = now_str
pulse['last_walk_at'] = now_str
pulse['last_walk'] = now_str
pulse['total_walks'] = pulse.get('total_walks', 0) + 1

# Update quality history
pulse['quality_history'].append(8.0)
if len(pulse['quality_history']) > 10:
    pulse['quality_history'] = pulse['quality_history'][-10:]

pulse['last_walk_insights'] = 3

# Cognitive pressure: walk just happened, so pressure drops
pulse['cognitive_pressure'] = max(0, pulse['cognitive_pressure'] - 3 * pulse['pressure_params']['release_per_insight'])

# Update affect
soul['affect']['primary'] = 'unsettled_fascination'
soul['affect']['intensity'] = 0.7
soul['mood'] = 'unsettled_fascination'
soul['mood_history'].append({'mood': 'unsettled_fascination', 'at': now_str})

# Personality traits
soul['personality_traits']['wonder'] = min(1.0, soul['personality_traits']['wonder'] + 0.01)
soul['personality_traits']['curiosity'] = min(1.0, soul['personality_traits']['curiosity'] + 0.01)

# Update walk quality avg
soul['walk_quality_avg'] = round(
    sum(pulse['quality_history']) / len(pulse['quality_history']), 1
)

# Calculate next interval
pressure = pulse['cognitive_pressure']
energy = soul['energy']

if pressure > 70:
    interval = 15
elif pressure < 20:
    interval = 60
elif energy < 20:
    interval = 90
else:
    interval = 30

pulse['current_interval_min'] = interval
pulse['next_scheduled'] = (now + timedelta(minutes=interval)).strftime('%Y-%m-%dT%H:%M:%S+08:00')

# Add evolved rule
soul['evolved_rules'].append(
    f"{now.strftime('%Y-%m-%d')}: 跨领域散步产生时间反方向洞察. Kolmogorov 级联=涌现的时间反方向(结构溶解vs结构凝聚). '内禀'属性可能只是条件未变时的别名——条件变化时内禀边界移动."
)

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, indent=2, ensure_ascii=False)

print(f"soul.json updated: walk #{pulse['total_walks']}, pressure={pressure:.1f}, next={interval}min")
