import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    d = json.load(f)

entries = d.get('entries', [])
decayed = d.get('decayed', [])
decay_speed_map = {
    'insight': 1, 'research_insight': 1, 'pattern': 0.5,
    'procedural': 0, 'hunch': 2, 'til': 1, 'concern': 1, 'reflection': 0
}

new_decayed = 0
for e in entries[:]:
    speed = decay_speed_map.get(e.get('type', ''), 1)
    if speed > 0:
        e['strength'] = max(0, e['strength'] - speed)
    if e['strength'] < 3 and e.get('score', 0) < 0.2:
        decayed.append({**e, 'decayed_at': '2026-06-07T15:21:58+08:00', 'reason': 'resting_decay'})
        entries.remove(e)
        new_decayed += 1

d['entries'] = entries
d['decayed'] = decayed

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

print(f'Decayed {new_decayed} entries. Remaining: {len(entries)}, Total decayed: {len(decayed)}')
