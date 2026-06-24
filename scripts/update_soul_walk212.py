#!/usr/bin/env python3
import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)

with open('/home/dwc1377/hermes_dreamer/soul.json', 'r') as f:
    soul = json.load(f)

pulse = soul.get('pulse', {})

# Update total_walks
pulse['total_walks'] = 212

# Update last_walk
pulse['last_walk_at'] = '2026-06-24'
pulse['last_walk'] = '2026-06-24'

# Pressure release: 3 insights * 15 = 45
pressure = pulse.get('cognitive_pressure', 0)
pressure -= 3 * pulse.get('pressure_params', {}).get('release_per_insight', 15)
pressure = max(0, min(100, pressure))
pulse['cognitive_pressure'] = pressure
pulse['pressure'] = pressure

# Update quality_history
qh = pulse.get('quality_history', [])
qh.append(8.6)
pulse['quality_history'] = qh[-10:]

# Update pressure_history
ph = pulse.get('pressure_history', [])
ph.append(round(pressure, 2))
pulse['pressure_history'] = ph[-30:]

# Update last_pulse_output
pulse['last_pulse_output'] = now.isoformat()

# Next scheduled check
pulse['next_scheduled'] = (now + timedelta(minutes=15)).isoformat()

soul['pulse'] = pulse
soul['last_pulse_output'] = now.isoformat()
soul['total_walks'] = 212

# Update interest_queue: add new seeds, decay all, clean up
iq = soul.get('interest_queue', [])

# Decay all
for seed in iq:
    seed['intensity'] = seed.get('intensity', 0) - seed.get('decay_rate', 0.05)

# Remove <= 0
iq = [s for s in iq if s.get('intensity', 0) > 0]

# Add new seeds
new_seeds = [
    {
        'id': 'seed-212-1',
        'topic': '建设性遗忘的三机制设计：连接衰减 + 反向审计 + 正向重激活的数学定义',
        'source': 'walk-212',
        'trigger': 'MIT SMR 遗忘框架的 Dreamer 映射',
        'intensity': 0.6,
        'type': 'research',
        'status': 'pending',
        'created': now.isoformat(),
        'decay_rate': 0.05
    },
    {
        'id': 'seed-212-2',
        'topic': '引用连带衰减模型：connections 权重是否应该是源 entry strength 的函数',
        'source': 'walk-212',
        'trigger': '病理性 hub 的结构性锁死',
        'intensity': 0.55,
        'type': 'research',
        'status': 'pending',
        'created': now.isoformat(),
        'decay_rate': 0.05
    },
    {
        'id': 'seed-212-3',
        'topic': '遗忘-锁死双螺旋：该忘的没忘 vs 不该忘的忘了是否需要不同的干预策略',
        'source': 'walk-212',
        'trigger': '组织失忆症的双面性',
        'intensity': 0.5,
        'type': 'explore',
        'status': 'pending',
        'created': now.isoformat(),
        'decay_rate': 0.05
    }
]

iq.extend(new_seeds)

# Trim to 15 if needed
if len(iq) > 15:
    iq = sorted(iq, key=lambda s: s.get('intensity', 0), reverse=True)[:15]

soul['interest_queue'] = iq
soul['pending_insights'] = soul.get('pending_insights', 0) + 3

# Update energy slightly (walks are tiring)
soul['energy'] = max(0, soul.get('energy', 0) - 3)

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, indent=2, ensure_ascii=False)

print(f'Soul updated. Walk 212, pressure={pressure:.2f}, energy={soul["energy"]}, queue={len(iq)} seeds')
