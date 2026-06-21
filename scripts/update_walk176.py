import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    data = json.load(f)

new_insights = [
    {
        "id": "ins-297",
        "type": "pattern",
        "content": "Dreamer DORMANT decay = cognitive Information Bottleneck: optimal compression is not uniform decay but differentiated compression based on each entry's predictive power for skeleton stability. beta_cognitive parameter controls compression strength, should dynamically relate to skeleton density and walk quality trends.",
        "strength": 5.0,
        "status": "active",
        "created": "2026-06-21T17:37:00+08:00",
        "source": "walk-176",
        "decay_rate": 0.05,
        "decayed_at": "",
        "resurrected_count": 0,
        "score": 0.0,
        "connections": [],
        "refs": [],
        "decay_speed": 1.0,
        "note": "IB framework mapped to Dreamer cognitive architecture"
    },
    {
        "id": "ins-298",
        "type": "pattern",
        "content": "Dreamer's Y (relevant information in IB framework) = skeleton stability. If an entry's disappearance does not change skeleton's citation patterns or structural integrity, its contribution to Y is zero - safe to compress. Y is not a static label but a dynamic system-level property.",
        "strength": 3.0,
        "status": "active",
        "created": "2026-06-21T17:37:00+08:00",
        "source": "walk-176",
        "decay_rate": 0.05,
        "decayed_at": "",
        "resurrected_count": 0,
        "score": 0.0,
        "connections": [],
        "refs": [],
        "decay_speed": 1.0,
        "note": "Y definition in Dreamer context"
    },
    {
        "id": "ins-299",
        "type": "pattern",
        "content": "Greedy IB Decay: retention_score = alpha*strength + beta*connections + gamma*citation_velocity. Adjust decay rate differentially based on retention_score. Better at preserving potentially valuable middle-layer entries than uniform decay.",
        "strength": 3.0,
        "status": "active",
        "created": "2026-06-21T17:37:00+08:00",
        "source": "walk-176",
        "decay_rate": 0.05,
        "decayed_at": "",
        "resurrected_count": 0,
        "score": 0.0,
        "connections": [],
        "refs": [],
        "decay_speed": 1.0,
        "note": "Implementation proposal, parameters need tuning"
    }
]

data.extend(new_insights)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added 3 insights. Total entries: {len(data)}")
