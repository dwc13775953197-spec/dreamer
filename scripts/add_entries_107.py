import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)
now_str = now.isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

new_entries = [
    {
        "id": "ins-090",
        "type": "insight",
        "strength": 3.0,
        "content": "AI agent forgetting crisis (Zylos 2026) reveals Dreamer's core problem: not too much forgetting, but too uniform forgetting. Letta Context Constitution proposes memory as constitution problem - deciding what to remember > remembering everything. Dreamer needs 'forgetting constitution': differential forgetting rates (based on premise stability, not strength) replacing current DORMANT uniform decay_rate.",
        "source": "walk-107",
        "created": now_str,
        "decay_rate": 1.0,
        "status": "active",
        "connections": ["ins-070", "ins-066", "pat-011", "pat-030"],
        "resurrected_count": 0,
        "score": 0.0,
        "refs": []
    },
    {
        "id": "ins-091",
        "type": "pattern",
        "strength": 3.0,
        "content": "Cumulative staleness is slow-motion catastrophic forgetting. Dreamer's 83 subconscious entries include 40 decayed, but some decayed entries may be valuable but not timely reinforced. Detecting staleness requires explicit representation of current skeleton (Mem0 2026 finding). Dreamer's skeleton (evolved_rules) has 49 rules - inspection cost increasing.",
        "source": "walk-107",
        "created": now_str,
        "decay_rate": 1.0,
        "status": "active",
        "connections": ["ins-068", "ins-069", "pat-011"],
        "resurrected_count": 0,
        "score": 0.0,
        "refs": []
    },
    {
        "id": "ins-092",
        "type": "insight",
        "strength": 3.0,
        "content": "Letta Context Repositories (2026.02) git-versioned memory model suggests Dreamer needs memory versioning: not just current state, but history of state transitions. evolved_rules has 49 rules without version tags - cannot trace conditions of generation, revision history, or current validity.",
        "source": "walk-107",
        "created": now_str,
        "decay_rate": 1.0,
        "status": "active",
        "connections": ["ins-058", "ins-068", "pat-011"],
        "resurrected_count": 0,
        "score": 0.0,
        "refs": []
    }
]

sub.extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, ensure_ascii=False, indent=2)

print(f"Added 3 entries. Total: {len(sub)}")
