import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/soul.json', 'r') as f:
    soul = json.load(f)

pulse = soul['pulse']

# Update pressure
pulse['cognitive_pressure'] = 76.70 - (3 * pulse['pressure_params']['release_per_insight'])
pulse['cognitive_pressure'] = max(0, min(100, pulse['cognitive_pressure']))

# Update walk tracking
pulse['last_walk_at'] = now
pulse['total_walks'] = 172
pulse['last_walk'] = now
pulse['last_walk_insights'] = 3
pulse['quality_history'] = pulse['quality_history'][-9:] + [8.4]
pulse['pressure_history'] = pulse['pressure_history'] + [76.70]

# Update mood
soul['affect'] = {
    "primary": "wonder",
    "secondary": "contemplative",
    "intensity": 0.85,
    "valence": 0.6,
    "arousal": 0.5,
    "rigor": 0.95
}
soul['mood'] = "wonder"
soul['mood_history'] = soul['mood_history'] + [{"mood": "wonder", "at": now}]
soul['energy'] = 34
soul['last_walk_at'] = now
soul['total_walks'] = 172
soul['last_walk'] = now
soul['pending_insights'] = soul.get('pending_insights', 0) + 3

# Update personality
soul['personality_traits']['rigor'] = min(3.0, soul['personality_traits']['rigor'] + 0.05)
soul['personality_traits']['wonder'] = min(2.0, soul['personality_traits']['wonder'] + 0.03)

# Decay interest queue
for seed in pulse['interest_queue']:
    seed['intensity'] = max(0, seed['intensity'] - seed.get('decay_rate', 0.05))

# Add new seeds
new_seeds = [
    {
        "id": "seed-172-1",
        "topic": "扩展表型在 AI agent 架构中的操作化：认知边界的可塑性",
        "source": "walk-172",
        "trigger": "extended phenotype mapping to Dreamer architecture",
        "intensity": 0.7,
        "type": "research",
        "status": "pending",
        "created": now,
        "decay_rate": 0.05
    },
    {
        "id": "seed-172-2",
        "topic": "生态位宽度作为 Dreamer 系统健康度的量化指标：特化 vs 泛化的韧性权衡",
        "source": "walk-172",
        "trigger": "niche width as system health metric",
        "intensity": 0.65,
        "type": "explore",
        "status": "pending",
        "created": now,
        "decay_rate": 0.05
    },
    {
        "id": "seed-172-3",
        "topic": "用户作为 Dreamer 环境的生态位建模：沉默/频繁/话题转换对系统可塑性的影响",
        "source": "walk-172",
        "trigger": "user as Dreamer environment",
        "intensity": 0.6,
        "type": "explore",
        "status": "pending",
        "created": now,
        "decay_rate": 0.05
    }
]

pulse['interest_queue'].extend(new_seeds)

# Remove zero-intensity seeds and keep max 15
pulse['interest_queue'] = [s for s in pulse['interest_queue'] if s['intensity'] > 0]
pulse['interest_queue'] = sorted(pulse['interest_queue'], key=lambda x: x['intensity'], reverse=True)[:15]

# Update next_scheduled (pressure > 70 -> 15 min interval)
pulse['next_scheduled'] = (datetime.now(tz) + timedelta(minutes=15)).isoformat()
pulse['current_interval_min'] = 15

# Update walk_quality_avg
pulse['walk_quality_avg'] = round(sum(pulse['quality_history']) / len(pulse['quality_history']), 2)

# Add new topic
if 'extended-phenotype' not in soul['topics']:
    soul['topics'].append('extended-phenotype')

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f"soul.json updated. total_walks={pulse['total_walks']}, pressure={pulse['cognitive_pressure']:.2f}")
print(f"interest_queue size: {len(pulse['interest_queue'])}")
print(f"quality_history: {pulse['quality_history']}")
