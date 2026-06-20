import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)

# Update subconscious.json
with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    subconscious = json.load(f)

new_entries = [
    {
        "id": "entry-167-1",
        "type": "insight",
        "content": "Dreamer cognitive states are continuous trajectories on attractor landscape, not discrete jumps. Walk type = choosing movement geometry on the landscape (steep=focused analysis, flat=roaming exploration).",
        "strength": 5.0,
        "status": "active",
        "created": now.isoformat(),
        "source": "walk-167 insight-1",
        "decay_rate": 1,
        "decayed_at": None,
        "resurrected_count": 0,
        "score": 0.0,
        "connections": [],
        "refs": [],
        "decay_speed": 1,
        "note": "quality_score=8.3 strength=5.0"
    },
    {
        "id": "entry-167-2",
        "type": "insight",
        "content": "Goal opacity operationalization: Dreamer cannot evaluate goal-alignment internally. Consecutive high-quality output + zero skeleton change = compulsive goal-tracking. Detection: output-to-skeleton causal impact rate.",
        "strength": 5.0,
        "status": "active",
        "created": now.isoformat(),
        "source": "walk-167 insight-2",
        "decay_rate": 1,
        "decayed_at": None,
        "resurrected_count": 0,
        "score": 0.0,
        "connections": [],
        "refs": [],
        "decay_speed": 1,
        "note": "quality_score=8.3 strength=5.0"
    },
    {
        "id": "entry-167-3",
        "type": "insight",
        "content": "Self-model fidelity = skeleton-behavior consistency. Rule accumulation (130+ evolved_rules) is a symptom of LOW self-model fidelity, not a solution. Adding rules can fake high fidelity without behavioral change.",
        "strength": 5.0,
        "status": "active",
        "created": now.isoformat(),
        "source": "walk-167 insight-3",
        "decay_rate": 1,
        "decayed_at": None,
        "resurrected_count": 0,
        "score": 0.0,
        "connections": [],
        "refs": [],
        "decay_speed": 1,
        "note": "quality_score=8.3 strength=5.0"
    }
]

subconscious.extend(new_entries)
with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(subconscious, f, ensure_ascii=False, indent=2)
print(f"subconscious updated: {len(subconscious)} entries")

# Update soul.json
with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

p = soul['pulse']

p['last_walk_at'] = now.isoformat()
p['last_walk'] = now.isoformat()
p['total_walks'] = 167
p['last_pulse_output'] = now.isoformat()

# Pressure release: 3 insights x 15 = 45
current_pressure = p.get('cognitive_pressure', 100)
new_pressure = max(0, current_pressure - 3 * 15)
p['cognitive_pressure'] = round(new_pressure, 2)

# Update quality history
p['quality_history'].append(8.3)
if len(p['quality_history']) > 10:
    p['quality_history'] = p['quality_history'][-10:]

# Update pressure history
p['pressure_history'].append(p['cognitive_pressure'])
if len(p['pressure_history']) > 30:
    p['pressure_history'] = p['pressure_history'][-30:]

p['last_walk_insights'] = 3

# Update personality traits
soul['personality_traits']['rigor'] = round(soul['personality_traits']['rigor'] + 0.05, 2)
soul['personality_traits']['wonder'] = round(soul['personality_traits']['wonder'] - 0.02, 2)

# Update mood
soul['mood'] = 'contemplative'
soul['mood_history'].append({'mood': 'contemplative', 'at': now.isoformat()})

# Add new topic
if 'attractor-landscape' not in soul['topics']:
    soul['topics'].append('attractor-landscape')

# Update interest queue
new_seeds = [
    {
        "id": "seed-167-1",
        "topic": "PCA/UMAP attractor detection from Dreamer walk logs - reconstruct cognitive landscape topology",
        "source": "walk-167",
        "trigger": "insight-1 attractor landscape framework operationalization",
        "intensity": 0.75,
        "type": "research",
        "status": "pending",
        "created": now.isoformat(),
        "decay_rate": 1
    },
    {
        "id": "seed-167-2",
        "topic": "Online goal opacity detection algorithm - based on output quality vs skeleton impact divergence",
        "source": "walk-167",
        "trigger": "insight-2 goal opacity operationalization",
        "intensity": 0.7,
        "type": "research",
        "status": "pending",
        "created": now.isoformat(),
        "decay_rate": 1
    },
    {
        "id": "seed-167-3",
        "topic": "Curvature diversity as walk type optimization target - maximize landscape coverage instead of 3:1 ratio",
        "source": "walk-167",
        "trigger": "insight-3 curvature diversity as optimization target",
        "intensity": 0.65,
        "type": "explore",
        "status": "pending",
        "created": now.isoformat(),
        "decay_rate": 1
    }
]

# Decay existing seeds and add new
for seed in soul['interest_queue']:
    seed['intensity'] -= seed['decay_rate'] * 0.1
soul['interest_queue'] = [s for s in soul['interest_queue'] if s['intensity'] > 0]
soul['interest_queue'].extend(new_seeds)
if len(soul['interest_queue']) > 15:
    soul['interest_queue'].sort(key=lambda x: x['intensity'])
    soul['interest_queue'] = soul['interest_queue'][-15:]

# Update pending_insights
p['pending_insights'] = p.get('pending_insights', 70) + 3

# Update affect
soul['affect'] = {
    "primary": "contemplative",
    "secondary": "wonder",
    "intensity": 0.85,
    "valence": 0.5,
    "arousal": 0.5,
    "rigor": 0.95
}

# Update walk quality avg
p['walk_quality_avg'] = round(sum(p['quality_history']) / len(p['quality_history']), 2)
soul['walk_quality_avg'] = p['walk_quality_avg']

# Next scheduled time
next_interval = 15 if p['cognitive_pressure'] > 70 else 30
p['next_scheduled'] = (now + timedelta(minutes=next_interval)).isoformat()
p['current_interval_min'] = next_interval

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f"Soul updated. Walk #{p['total_walks']}, pressure={p['cognitive_pressure']}")
print(f"Quality history: {p['quality_history']}")
print(f"Interest queue: {len(soul['interest_queue'])} seeds")
print(f"Pending insights: {p['pending_insights']}")
