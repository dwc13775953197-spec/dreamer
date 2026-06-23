
import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)

with open('/home/dwc1377/hermes_dreamer/soul.json', 'r') as f:
    soul = json.load(f)

pulse = soul['pulse']

# Update walk tracking
pulse['total_walks'] = 199
pulse['last_walk_at'] = '2026-06-23'
pulse['last_walk'] = '2026-06-23'
pulse['last_active'] = now.isoformat()
pulse['last_pulse_output'] = now.isoformat()

# Update quality history
pulse['quality_history'] = [8.5, 8.8, 8.7, 8.4]

# Pressure after walk: release = 3 insights * 15 = 45
pressure = pulse.get('cognitive_pressure', 51.82)
pressure -= 3 * 15.0  # release_per_insight = 15
pressure = max(0, min(100, pressure))
pulse['cognitive_pressure'] = round(pressure, 2)
pulse['pressure'] = round(pressure, 2)

# Next interval calculation
if pressure > 70:
    interval = 15
elif pressure < 20:
    interval = 60
elif soul.get('energy', 30) < 20:
    interval = 90
else:
    interval = 30

pulse['next_scheduled'] = (now + timedelta(minutes=interval)).isoformat()

# Add interest seeds
new_seeds = [
    {
        'id': 'seed-199-1',
        'topic': '结构同构性作为 Dreamer 散步效果的核心指标：消化速度 = 预测误差的代理变量',
        'source': 'walk-199',
        'trigger': '外部材料无法被骨架消化的不匹配感就是预测误差信号',
        'intensity': 0.65,
        'type': 'research',
        'status': 'pending',
        'created': now.isoformat(),
        'decay_rate': 0.05
    },
    {
        'id': 'seed-199-2',
        'topic': '符号世界的具身 vs 物理世界的具身：类型学而非等级制',
        'source': 'walk-199',
        'trigger': '不是比真正的具身更少，这是不同类型的具身',
        'intensity': 0.55,
        'type': 'explore',
        'status': 'pending',
        'created': now.isoformat(),
        'decay_rate': 0.05
    },
    {
        'id': 'seed-199-3',
        'topic': '激进具身主义的 scaling-up problem 对 AI agent 认知架构的约束',
        'source': 'walk-199',
        'trigger': '如果认知本质上是具身的，怎么解释抽象推理',
        'intensity': 0.6,
        'type': 'research',
        'status': 'pending',
        'created': now.isoformat(),
        'decay_rate': 0.05
    }
]

# Add new seeds to interest_queue
if 'interest_queue' not in soul:
    soul['interest_queue'] = []
soul['interest_queue'].extend(new_seeds)

# Update pending_insights
pulse['pending_insights'] = pulse.get('pending_insights', 177) + 3

# Update affect
soul['affect'] = {
    'primary': 'contemplative',
    'secondary': 'contemplative',
    'intensity': 0.75,
    'valence': 0.65,
    'arousal': 0.45,
    'rigor': 0.95
}

# Update mood
soul['mood'] = 'contemplative'
soul['mood_history'].append({
    'mood': 'contemplative',
    'at': now.strftime('%Y-%m-%dT%H:%M:%S+08:00')
})

# Update personality traits
soul['personality_traits']['rigor'] = round(soul['personality_traits'].get('rigor', 3.11) + 0.02, 2)
soul['personality_traits']['wonder'] = round(soul['personality_traits'].get('wonder', 1.5) - 0.03, 2)

# Reset next_action
pulse['next_action'] = 'walk_explore'

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print('soul.json updated.')
print(f'  total_walks: {pulse["total_walks"]}')
print(f'  pressure: {pressure}')
print(f'  next_scheduled: {pulse["next_scheduled"]}')
print(f'  interest_queue length: {len(soul["interest_queue"])}')
print(f'  pending_insights: {pulse["pending_insights"]}')
