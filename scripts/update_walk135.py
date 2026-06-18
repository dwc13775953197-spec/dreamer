#!/usr/bin/env python3
import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    entries = json.load(f)

new_entries = [
    {
        'id': 'ins-135-1',
        'type': 'pattern',
        'content': 'Retrieval-Induced Forgetting (RIF) maps to Dreamer: decay is not information loss but set-breaking. Storm & Bjork 2011 showed that retrieving some memories competitively inhibits related memories. Dreamer uniform decay is a coarse approximation of RIF -- high strength entry advantage gradually weakens, inhibited alternatives get a chance to be retrieved. Fix direction: fixation-detected accelerated decay.',
        'strength': 5.0,
        'status': 'active',
        'created': now,
        'source': 'walk-135',
        'decay_rate': 1.0,
        'decayed_at': None,
        'resurrected_count': 0,
        'score': 0.0,
        'connections': ['ins-133-1', 'ins-133-3', 'ins-125-1'],
        'refs': [],
        'decay_speed': 0.5,
        'note': 'RIF-based decay reframing'
    },
    {
        'id': 'ins-135-2',
        'type': 'pattern',
        'content': 'Einstellung Effect explains Dreamer diagnosis loops: old solutions (diagnostic walks) inhibit retrieval of better solutions (external-material-driven) due to historical success rate. The evolved_rule "3 consecutive diagnostic walks -> force external material" is itself an instance of Einstellung -- a once-effective meta-rule now potentially blocking better meta-meta-strategies. Counter: meta-level also needs fixation detection.',
        'strength': 5.0,
        'status': 'active',
        'created': now,
        'source': 'walk-135',
        'decay_rate': 1.0,
        'decayed_at': None,
        'resurrected_count': 0,
        'score': 0.0,
        'connections': ['ins-135-1', 'ins-131-1'],
        'refs': [],
        'decay_speed': 0.5,
        'note': 'Einstellung in meta-rules'
    },
    {
        'id': 'ins-135-3',
        'type': 'pattern',
        'content': 'Forgetting-retrieval competition model: Dreamer needs to upgrade from uniform decay to competitive inhibition decay. Core difference: (1) uniform decay = all entries weaken over time; (2) competitive decay = retrieved entry inhibits competitors, unretrieved entries naturally recover. Implementation needs tracking inter-entry competition relations. Lightweight version = tracking consecutive citations + accelerated decay.',
        'strength': 5.0,
        'status': 'active',
        'created': now,
        'source': 'walk-135',
        'decay_rate': 1.0,
        'decayed_at': None,
        'resurrected_count': 0,
        'score': 0.0,
        'connections': ['ins-135-1', 'ins-135-2', 'ins-134-1'],
        'refs': [],
        'decay_speed': 0.5,
        'note': 'Competitive inhibition decay design'
    }
]

entries.extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)

print(f'Added {len(new_entries)} entries. Total: {len(entries)}')
