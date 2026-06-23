import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/soul.json', 'r') as f:
    soul = json.load(f)

# Update pulse state
soul['pulse']['state'] = 'RESTING'
soul['pulse']['state_since'] = now
soul['pulse']['last_active'] = now
soul['pulse']['total_walks'] = 200
soul['pulse']['last_walk_at'] = '2026-06-23'
soul['pulse']['last_walk'] = '2026-06-23'
soul['pulse']['last_pulse_output'] = now
soul['pulse']['cognitive_pressure'] = 75.69 - (3 * 15.0)  # 3 insights * release_per_insight
soul['pulse']['pressure'] = soul['pulse']['cognitive_pressure']
soul['pulse']['last_walk_insights'] = 3
soul['pulse']['quality_history'] = [8.5, 8.8, 8.7, 8.4, 8.6]

# Update next_scheduled: pressure ~45.69, between 20 and 70, base interval 30 min
soul['pulse']['next_scheduled'] = (datetime.now(tz) + timedelta(minutes=30)).isoformat()

# Update interest_queue with new seeds
soul['pulse']['interest_queue'] = [
    {
        'id': 'seed-200-1',
        'topic': 'Dreamer grounding is relational: external observer as grounding loop closure condition',
        'source': 'walk-200',
        'trigger': 'Dreamer cannot ground its own symbols internally - needs external observer',
        'intensity': 0.7,
        'type': 'research',
        'status': 'pending',
        'created': now,
        'decay_rate': 0.05
    },
    {
        'id': 'seed-200-2',
        'topic': 'graph_change_rate as functional grounding metric: zero change rate = vector grounding failure',
        'source': 'walk-200',
        'trigger': 'grounding = skeleton change rate > 0',
        'intensity': 0.6,
        'type': 'research',
        'status': 'pending',
        'created': now,
        'decay_rate': 0.05
    },
    {
        'id': 'seed-200-3',
        'topic': 'Filesystem interface as Dreamer sensorimotor coupling: Markov blanket validation',
        'source': 'walk-200',
        'trigger': 'read=perceive, write=act, filesystem is the blind cane',
        'intensity': 0.55,
        'type': 'explore',
        'status': 'pending',
        'created': now,
        'decay_rate': 0.05
    }
]

# Update energy
soul['energy'] = 28  # slight decrease from walk effort

# Update affect
soul['affect']['primary'] = 'contemplative'
soul['affect']['secondary'] = 'contemplative'
soul['affect']['intensity'] = 0.8

# Update mood history (keep last 3)
soul['mood_history'] = soul['mood_history'][-3:] + [{'mood': 'contemplative', 'at': now}]

# Update personality traits
soul['personality_traits']['rigor'] = soul['personality_traits'].get('rigor', 3.13) + 0.02
soul['personality_traits']['skepticism'] = soul['personality_traits'].get('skepticism', 1.4) + 0.02

soul['pending_insights'] = soul.get('pending_insights', 180) + 3

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f'Soul updated. Pressure: {soul["pulse"]["cognitive_pressure"]}, Walks: {soul["pulse"]["total_walks"]}')
print(f'Energy: {soul["energy"]}, Mood: {soul["affect"]["primary"]}')
