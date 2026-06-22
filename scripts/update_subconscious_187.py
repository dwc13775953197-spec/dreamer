import json
from datetime import datetime, timezone, timedelta

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    subconscious = json.load(f)

now = datetime.now(timezone(timedelta(hours=8)))
now_iso = now.isoformat()

new_insights = [
    {
        'id': 'insight-187-1',
        'type': 'insight',
        'content': 'Forgetting as complement of reactivation: Albouy selective reactivation shows brain needs no forgetting strategy. Natural decay of non-reactivated memories IS forgetting. Dreamer Eviction lever may be design redundancy.',
        'strength': 3.0,
        'status': 'active',
        'created': now_iso,
        'source': 'walk-187',
        'decay_rate': 0.05,
        'decayed_at': 0,
        'resurrected_count': 0,
        'connections': ['insight-182-2', 'insight-183-1', 'ins-101']
    },
    {
        'id': 'insight-187-2',
        'type': 'insight',
        'content': 'Bjork desirable difficulty operationalized in Dreamer: inverse citation frequency x content quality = DORMANT reactivation priority. Low-citation high-value entries should be reactivated first to break anchoring.',
        'strength': 3.0,
        'status': 'active',
        'created': now_iso,
        'source': 'walk-187',
        'decay_rate': 0.05,
        'decayed_at': 0,
        'resurrected_count': 0,
        'connections': ['insight-179-2', 'seed-187-2']
    },
    {
        'id': 'insight-187-3',
        'type': 'insight',
        'content': 'Bio-validity gap in Forgetting operation: engineering forgetting (capacity eviction/TTL/relevance filter) vs biological natural forgetting (passive decay) differ systematically. Dreamer DORMANT is closer to biology and should not copy engineering forgetting models.',
        'strength': 3.0,
        'status': 'active',
        'created': now_iso,
        'source': 'walk-187',
        'decay_rate': 0.05,
        'decayed_at': 0,
        'resurrected_count': 0,
        'connections': ['insight-182-1', 'insight-186-1']
    }
]

subconscious.extend(new_insights)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(subconscious, f, indent=2, ensure_ascii=False)

print(f'Done. Added {len(new_insights)} insights. Total: {len(subconscious)}')
