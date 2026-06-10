import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)

with open('/home/dwc1377/hermes_dreamer/soul.json', 'r') as f:
    soul = json.load(f)

pulse = soul['pulse']
pulse['last_walk_at'] = now.isoformat()
pulse['last_active'] = now.isoformat()
pulse['total_walks'] = pulse.get('total_walks', 43) + 1

pressure = 40.8
pressure -= 5 * 15
pressure = max(0, min(100, pressure))
pulse['cognitive_pressure'] = round(pressure, 1)

pulse['quality_history'].append(8.3)
pulse['quality_history'] = pulse['quality_history'][-10:]
pulse['last_walk_insights'] = 5

soul['mood'] = 'unsettled_fascination'
soul['affect']['intensity'] = 0.98
soul['last_walk'] = now.isoformat()
soul['personality_traits']['wonder'] = 0.99

soul['evolved_rules'].append(
    '2026-06-10: Skeleton is cognitive lattice. DORMANT over-compression creates cognitive glass. '
    'New insights follow nucleation-growth model. Cognitive phase diagram (temp x pressure x time-density) '
    'predicts behavioral state. Walks = cognitive annealing (gentle rearrangement to release stress).'
)

consumed = soul.get('diversity_seeds_consumed', [])
if 'seed-div-20260610' not in consumed:
    consumed.append('seed-div-20260610')
soul['diversity_seeds_consumed'] = consumed

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f'Updated soul.json: walk #{pulse["total_walks"]}, pressure={pulse["cognitive_pressure"]}')
