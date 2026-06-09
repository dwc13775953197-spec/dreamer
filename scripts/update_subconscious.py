import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

# Decay all entries
for entry in sub['entries']:
    if entry['status'] == 'active' and entry.get('decay_speed', 0) > 0:
        entry['strength'] = max(0, entry['strength'] - entry['decay_speed'])
        if entry['strength'] < 3 and entry['status'] == 'active':
            entry['status'] = 'decayed'
            entry['decayed_at'] = now
            entry['decay_reason'] = 'natural_decay'

# Add new insights
new_entries = [
    {
        'id': 'ins-188',
        'type': 'insight',
        'source': 'walk-057',
        'created': now,
        'strength': 1.0,
        'decay_speed': 0.5,
        'pattern_id': 'pat-030',
        'text': 'Diversity-stability paradox answer is structure not quantity: May 1972 proved diversity destabilizes under random interactions, but real ecosystems have weak interactions, modularity, directional cascades. Maps to DORMANT: optimal attention distribution is modular diversity not uniformity - local concentration allowed (functional hubs), global integration maintained (cross-module weak connections). Corrects walk-056: distance should be discrete (intra vs cross-module) not continuous.',
        'refs': ['walk-057', 'pat-030', 'pat-001', 'seed-157', 'seed-152'],
        'note': 'walk-057 cross-ecology: diversity-stability paradox x cognitive attention',
        'status': 'active',
        'resurrected_count': 0,
        'score': 0.6
    },
    {
        'id': 'ins-189',
        'type': 'insight',
        'source': 'walk-057',
        'created': now,
        'strength': 0.8,
        'decay_speed': 0.5,
        'pattern_id': 'pat-001',
        'text': 'Citation loops may be stability threat not vitality: infinite nutrient cycling causes oscillation collapse in ecosystems. DORMANT pattern clusters that cite each other may form positive feedback loops - need funnel to break cycles. pat-001/pat-011/pat-014 cluster needs checking for over-reinforcement.',
        'refs': ['walk-057', 'pat-001', 'pat-011', 'pat-014'],
        'note': 'walk-057: citation loops as stability threat',
        'status': 'active',
        'resurrected_count': 0,
        'score': 0.55
    },
    {
        'id': 'ins-190',
        'type': 'insight',
        'source': 'walk-057',
        'created': now,
        'strength': 0.5,
        'decay_speed': 0.5,
        'pattern_id': 'pat-001',
        'text': 'pat-001 as hub may be functional (keystone species) not pathological Matthew effect. Distinguishing criterion: does the hub suppress other modules growth? If pat-001s high citation coexists with other modules getting enough attention = functional hub. If other modules cant grow because pat-001 monopolizes attention = pathological. Needs empirical data.',
        'refs': ['walk-057', 'pat-001', 'seed-152', 'seed-159'],
        'note': 'walk-057: keystone species concept applied to pattern hubs',
        'status': 'active',
        'resurrected_count': 0,
        'score': 0.5
    },
    {
        'id': 'ref-025',
        'type': 'reflection',
        'source': 'walk-057',
        'created': now,
        'strength': 5.0,
        'decay_speed': 0,
        'relevance': 0.8,
        'text': 'Reflection - 2026-06-09 Walk-057: May paradox and cognitive attention allocation. Diversity itself does not determine stability - interaction structure does (weak interactions + modularity + directional cascades). Optimal attention distribution is modular diversity not uniformity. Corrects walk-056 distance-weighted citation: distance should be discrete (intra vs cross-module). Key finding: pat-001 may be keystone species not Matthew effect victim.',
        'refs': ['walk-057', 'pat-001', 'pat-030', 'pat-011', 'pat-014', 'seed-157', 'seed-152', 'ins-188', 'ins-189', 'ins-190'],
        'status': 'active',
        'resurrected_count': 0,
        'score': 0.8
    }
]

sub['entries'].extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, ensure_ascii=False, indent=2)

print(f'subconscious.json updated: {len(new_entries)} new entries')
