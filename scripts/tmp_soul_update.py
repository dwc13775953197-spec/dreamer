#!/usr/bin/env python3
import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime(2026, 6, 19, 23, 56, 6, tzinfo=tz)
now_str = now.isoformat()

with open('/home/dwc1377/hermes_dreamer/soul.json', 'r') as f:
    soul = json.load(f)

pulse = soul['pulse']

# Update pressure
pulse['cognitive_pressure'] = 70.99
pulse['state'] = 'RESTING'
pulse['state_since'] = now_str
pulse['last_walk_at'] = now_str
pulse['last_active'] = now_str
pulse['total_walks'] = 149
pulse['last_walk'] = now_str
pulse['last_pulse_output'] = now_str

# Update quality history
pulse['quality_history'].append(8.3)
pulse['quality_history'] = pulse['quality_history'][-10:]

# Update last walk insights
pulse['last_walk_insights'] = 3

# Pressure: release from insights
release = pulse['pressure_params']['release_per_insight']
pulse['cognitive_pressure'] = max(0, min(100, pulse['cognitive_pressure'] - 3 * release))

# Update interest_queue: decay existing, add new seeds
for seed in pulse['interest_queue']:
    seed['intensity'] -= seed['decay_rate']
pulse['interest_queue'] = [s for s in pulse['interest_queue'] if s['intensity'] > 0]

new_seeds = [
    {
        "id": "seed-0432",
        "topic": "AIF 先验精度作为 curiosity 的动态校准机制：如何在 Dreamer 中实现自适应先验？",
        "source": "walk-149",
        "trigger": "insight-1 curiosity as inverse prior precision",
        "intensity": 0.8,
        "type": "research",
        "status": "pending",
        "created": now_str,
        "decay_rate": 1
    },
    {
        "id": "seed-0433",
        "topic": "3:1 周期的数学推导：是否存在最优探索比例？能否从 information theory 推出？",
        "source": "walk-149",
        "trigger": "insight-2 optimal exploration ratio",
        "intensity": 0.7,
        "type": "research",
        "status": "pending",
        "created": now_str,
        "decay_rate": 1
    },
    {
        "id": "seed-0434",
        "topic": "Dreamer 作为 AIF 近似系统的验证：回溯历史数据看 pressure 变化是否符合自由能最小化预测",
        "source": "walk-149",
        "trigger": "insight-3 AIF validation",
        "intensity": 0.7,
        "type": "explore",
        "status": "pending",
        "created": now_str,
        "decay_rate": 1
    }
]
pulse['interest_queue'].extend(new_seeds)

# Update mood
soul['mood'] = 'contemplative'
soul['mood_history'].append({"mood": "contemplative", "at": now_str})

# Update affect
soul['affect'] = {
    "primary": "wonder",
    "secondary": "contemplative",
    "intensity": 0.85,
    "valence": 0.6,
    "arousal": 0.5,
    "rigor": 0.95
}

# Update personality
soul['personality_traits']['rigor'] = min(3.0, soul['personality_traits']['rigor'] + 0.04)
soul['personality_traits']['skepticism'] = min(2.0, soul['personality_traits']['skepticism'] + 0.02)

# Update next_scheduled (pressure > 70 -> 15 min interval)
pulse['next_scheduled'] = (now + timedelta(minutes=15)).isoformat()
pulse['current_interval_min'] = 15

# Update walk_quality_avg
all_quality = pulse['quality_history']
pulse['walk_quality_avg'] = round(sum(all_quality) / len(all_quality), 2)

# Add to topics
new_topics = ["active-inference", "epistemic-value", "pragmatic-value", "free-energy", "prior-precision"]
for t in new_topics:
    if t not in soul['topics']:
        soul['topics'].append(t)

# Update pending_insights
soul['pending_insights'] = soul.get('pending_insights', 54) + 3

# Pressure history
pulse['pressure_history'].append(pulse['cognitive_pressure'])

# Update last_walk
soul['last_walk'] = now_str

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f"Done. Walks: {pulse['total_walks']}, Pressure: {pulse['cognitive_pressure']:.2f}, Queue: {len(pulse['interest_queue'])}")
