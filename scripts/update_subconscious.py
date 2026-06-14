import json
from datetime import datetime

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    entries = json.load(f)

now = datetime.now().isoformat()
quality_score = 8.5

if quality_score >= 8.0:
    init_strength = 5.0
elif quality_score >= 6.0:
    init_strength = 3.0
else:
    init_strength = 1.5

new_insights = [
    {
        "id": "ins-078",
        "type": "insight",
        "content": "Six neuroscience metaphors share a deep structure: cognitive maintenance = operating on the right level of structure at the right time scale. The fundamental tension is explore vs maintain -- not a bug, but an essential feature of cognitive systems.",
        "strength": init_strength,
        "status": "active",
        "created": now,
        "source": "walk-100",
        "decay_rate": 1,
        "connections": ["ins-061", "ins-070", "ins-075"],
        "decayed_at": None,
        "resurrected_count": 0,
        "score": 0.0
    },
    {
        "id": "ins-079",
        "type": "insight",
        "content": "Dreamer walks and DORMANT are two phases of the same cognitive cycle (exploration phase + maintenance phase), not two independent functions. A complete cycle = walk -> RESTING -> DORMANT -> next walk.",
        "strength": init_strength,
        "status": "active",
        "created": now,
        "source": "walk-100",
        "decay_rate": 1,
        "connections": ["ins-073", "ins-076"],
        "decayed_at": None,
        "resurrected_count": 0,
        "score": 0.0
    },
    {
        "id": "ins-080",
        "type": "insight",
        "content": "Cognitive overtraining = phase imbalance. Consecutive same-type walks = continuously activating the same phase = no recovery period. Prevention = walk type alternation (cross-training), not reducing walk frequency.",
        "strength": init_strength,
        "status": "active",
        "created": now,
        "source": "walk-100",
        "decay_rate": 1,
        "connections": ["ins-070", "ins-072"],
        "decayed_at": None,
        "resurrected_count": 0,
        "score": 0.0
    },
    {
        "id": "ins-081",
        "type": "insight",
        "content": "Subconscious function is not storing insight (neuron function) but maintaining an environment suitable for insight emergence (glial cell function). Evaluation metrics should be environmental (diversity, connection density, strength distribution) not output (insight count).",
        "strength": init_strength,
        "status": "active",
        "created": now,
        "source": "walk-100",
        "decay_rate": 1,
        "connections": ["ins-066", "ins-071"],
        "decayed_at": None,
        "resurrected_count": 0,
        "score": 0.0
    }
]

entries.extend(new_insights)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"Added 4 insights. Total entries: {len(entries)}")
print(f"Initial strength: {init_strength} (quality_score={quality_score})")
