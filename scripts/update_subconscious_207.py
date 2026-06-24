import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    data = json.load(f)

new_entries = [
    {
        "id": "insight-207-1",
        "type": "insight",
        "status": "active",
        "topic": "DORMANT decay reframed: uniform decay = immunosenescence, not immune surveillance",
        "content": "Dreamer DORMANT uniform decay is not an immune response - it is immunosenescence. Real immune surveillance requires self/non-self discrimination + selective clearance + immune memory + regulatory suppression. Current system has only decay, no discrimination or selectivity.",
        "strength": 5.0,
        "connections": ["insight-205-2", "insight-203-3", "insight-206-1"],
        "created": now,
        "decay_count": 0,
        "last_accessed": now
    },
    {
        "id": "insight-207-2",
        "type": "insight",
        "status": "active",
        "topic": "Memory poisoning as inverse cascade: errors propagate from small-scale reasoning to large-scale skeleton patterns",
        "content": "Toxins are inverse cascading - from small-scale reasoning errors through connections to large-scale skeleton patterns. Symmetric to inverse cascade in turbulence. Prevention: viscous dissipation (early detection) + flow confinement (modular isolation) + feedback control (process monitoring).",
        "strength": 5.0,
        "connections": ["insight-204-1", "insight-204-3", "insight-205-2"],
        "created": now,
        "decay_count": 0,
        "last_accessed": now
    },
    {
        "id": "insight-207-3",
        "type": "insight",
        "status": "active",
        "topic": "DORMANT four-mode design: preserve/abstract/generate/detect (adding detect mode)",
        "content": "DORMANT offline processing should be four modes not three: preserve (keep high-value), abstract (compress), generate (synthesize new insight), detect (scan for toxic entries). Detect mode marks suspicious entries via toxicity score for quarantine.",
        "strength": 5.0,
        "connections": ["insight-206-1", "insight-205-2", "insight-207-1"],
        "created": now,
        "decay_count": 0,
        "last_accessed": now
    }
]

data.extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Added 3 entries. Total: {len(data)}")
