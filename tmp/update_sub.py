import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)

with open('subconscious.json', 'r') as f:
    sub = json.load(f)

new_entries = [
    {
        'id': 'ins-163-1',
        'type': 'insight',
        'content': 'Dreamer is already a stigmergic system: walk logs are pheromone traces guiding subsequent walks. The question is not "whether" but whether parameters are optimal (decay rate, deposition strength, response threshold).',
        'strength': 5.0,
        'status': 'active',
        'created': now.isoformat(),
        'source': 'walk-163',
        'decay_rate': 1.0,
        'connections': [],
        'refs': []
    },
    {
        'id': 'ins-163-2',
        'type': 'insight',
        'content': 'Trace decay rate should be citation-frequency modulated: more-cited entries decay slower (pheromone highways). Current uniform decay is suboptimal parameter.',
        'strength': 5.0,
        'status': 'active',
        'created': now.isoformat(),
        'source': 'walk-163',
        'decay_rate': 1.0,
        'connections': [],
        'refs': []
    },
    {
        'id': 'ins-163-3',
        'type': 'insight',
        'content': 'Dreamer exhibits stigmergic phase transitions: silent phase (glass skeleton), saturated phase (RAM-as-disk), adaptive phase (critical point). Adaptive phase is the target -- dynamic balance between silence and saturation.',
        'strength': 5.0,
        'status': 'active',
        'created': now.isoformat(),
        'source': 'walk-163',
        'decay_rate': 1.0,
        'connections': [],
        'refs': []
    }
]

sub.extend(new_entries)

with open('subconscious.json', 'w') as f:
    json.dump(sub, f, indent=2, ensure_ascii=False)

print(f'subconscious.json updated: added 3 entries, total={len(sub)}')
