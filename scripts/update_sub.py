import json
from datetime import datetime, timezone, timedelta

now = datetime.now(timezone(timedelta(hours=8)))
now_iso = now.isoformat()

new_insight = {
    "id": "ins-new-230-1",
    "type": "insight",
    "content": "DORMANT three-source PE generation: projection earthquake PE (coordinate shifts disorient old insights), coherence decay PE (gap insight淘汰 triggers neighbor锚点 loss), hitting blind spot PE (coordinate incommensurability exposes projection inadequacy). Only hitting blind spot PE drives real structural update. Current DORMANT lacks explicit PE type identification.",
    "strength": 4.0,
    "score": 0.72,
    "status": "active",
    "created": now_iso,
    "source": "walk-230",
    "resurrected_count": 0,
    "refs": [],
    "decay_speed": 1.0,
    "connections": ["ins-215-1", "ins-223-001", "ins-224-3"]
}

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

sub.append(new_insight)

for e in sub:
    if e.get('status') == 'active' and 'decay_speed' in e:
        decay = e.get('decay_speed', 0.5) * 0.01
        e['strength'] = max(e.get('strength', 0) - decay, 0)
        e['score'] = min(max(e['strength'] / 5.0, 0), 1.0)

print(f"Added {new_insight['id']}, total entries: {len(sub)}")

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, ensure_ascii=False, indent=2)

print("Done")