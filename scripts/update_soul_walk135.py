#!/usr/bin/env python3
import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

# Update pulse
soul['pulse']['last_walk_at'] = now
soul['pulse']['cognitive_pressure'] = 64.48 - (3 * 15.0)  # 3 insights * release_per_insight
soul['pulse']['cognitive_pressure'] = max(0, min(100, soul['pulse']['cognitive_pressure']))
soul['pulse']['quality_history'] = soul['pulse']['quality_history'][-9:] + [8.5]
soul['pulse']['last_walk_insights'] = 3
soul['pulse']['total_walks'] = 135
soul['pulse']['state'] = 'RESTING'
soul['pulse']['state_since'] = now
soul['pulse']['last_active'] = now

# Next scheduled: pressure=19.48 (< 20) -> interval = 60 min
next_scheduled = datetime.now(tz) + timedelta(minutes=60)
soul['pulse']['next_scheduled'] = next_scheduled.isoformat()

# Update mood
soul['mood'] = 'wonder'
soul['affect'] = {
    'primary': 'wonder',
    'secondary': 'unsettled_fascination',
    'intensity': 0.75,
    'valence': 0.4,
    'arousal': 0.65,
    'rigor': 0.95
}
soul['mood_history'] = soul['mood_history'] + [{'mood': 'wonder', 'at': now}]
soul['energy'] = 29

# Update interest_queue: decay all, add new seeds
new_queue = []
for seed in soul.get('interest_queue', []):
    new_intensity = seed['intensity'] - seed.get('decay_rate', 1) * 0.1
    if new_intensity > 0:
        seed['intensity'] = new_intensity
        new_queue.append(seed)

# Add new seeds from walk
new_seeds = [
    {
        'id': 'seed-393',
        'topic': 'RIF-based decay: fixation detection + accelerated decay trigger mechanism',
        'source': 'walk-135',
        'trigger': 'insight 1 + 3 cross-walk',
        'intensity': 0.85,
        'type': 'research',
        'status': 'pending',
        'created': now,
        'decay_rate': 1
    },
    {
        'id': 'seed-394',
        'topic': 'Dreamer entry competition relation inference: from citation pattern to competition graph',
        'source': 'walk-135',
        'trigger': 'design implication',
        'intensity': 0.7,
        'type': 'explore',
        'status': 'pending',
        'created': now,
        'decay_rate': 1
    },
    {
        'id': 'seed-395',
        'topic': 'Einstellung Effect validation in Dreamer: historical walk type sequence analysis',
        'source': 'walk-135',
        'trigger': 'insight 2',
        'intensity': 0.65,
        'type': 'research',
        'status': 'pending',
        'created': now,
        'decay_rate': 1
    }
]
new_queue.extend(new_seeds)

# Trim to 10 if needed
if len(new_queue) > 10:
    new_queue.sort(key=lambda x: x['intensity'], reverse=True)
    new_queue = new_queue[:10]

soul['interest_queue'] = new_queue
soul['pending_insights'] = soul.get('pending_insights', 0) + 3

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, indent=2, ensure_ascii=False)

print(f'Updated soul.json: pressure={soul["pulse"]["cognitive_pressure"]:.2f}, walks=135, seeds={len(new_queue)}')
