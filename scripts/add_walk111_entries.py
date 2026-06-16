import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    data = json.load(f)

print("Current entries:", len(data))

new_entries = [
    {
        "id": "ins-110",
        "type": "insight",
        "content": "35-minute barrier is a physical constraint of cognitive systems, not an engineering defect. Any finite system has a coherence time window. Dreamer's walk design should actively use this constraint (cognitive budget + proactive ending) rather than trying to surpass it.",
        "strength": 3.0,
        "score": 0.3,
        "status": "active",
        "created": "2026-06-16T14:30:00+08:00",
        "source": "walk-111",
        "decay_rate": 1
    },
    {
        "id": "ins-111",
        "type": "insight",
        "content": "Temporal grain is a fundamental design parameter of cognitive architecture, determining the complexity of tasks a system can handle. Second-level systems cannot handle hour-level tasks. Dreamer's temporal grain is the pulse - each walk is a discrete cognitive unit.",
        "strength": 3.0,
        "score": 0.3,
        "status": "active",
        "created": "2026-06-16T14:30:00+08:00",
        "source": "walk-111",
        "decay_rate": 1
    },
    {
        "id": "pat-031",
        "type": "pattern",
        "content": "Cognitive budget mechanism: each walk has an implicit budget at the concept level (concept count x connection depth). Quality drops off a cliff when budget is exceeded. Walks should end proactively when budget is spent. Different walk types have different coherence time windows - exploratory short, analytical long.",
        "strength": 3.0,
        "score": 0.3,
        "status": "active",
        "created": "2026-06-16T14:30:00+08:00",
        "source": "walk-111",
        "decay_rate": 0.5
    }
]

data.extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Added 3 entries. Total now:", len(data))
