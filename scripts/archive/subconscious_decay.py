import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    data = json.load(f)

entries = data['entries']
decayed = data['decayed']
moved = []

for entry in entries:
    if entry.get('status') == 'decayed':
        continue
    ds = entry.get('decay_speed', 0)
    if ds <= 0:
        continue
    old_strength = entry['strength']
    new_strength = old_strength - ds
    if new_strength <= 0:
        # Move to decayed
        entry['status'] = 'decayed'
        entry['decayed_at'] = '2026-06-08T10:26:56+08:00'
        entry['strength'] = 0
        entry['decay_reason'] = 'natural_decay'
        decayed.append(entry)
        moved.append(f"  {entry['id']}: {old_strength} → 0 (moved to decayed)")
    else:
        entry['strength'] = new_strength
        moved.append(f"  {entry['id']}: {old_strength} → {new_strength}")

# Remove decayed entries from active list
data['entries'] = [e for e in data['entries'] if e.get('status') != 'decayed']
data['decayed'] = decayed

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Decay applied:")
for m in moved:
    print(m)
print(f"\nActive entries: {len(data['entries'])}")
print(f"Decayed entries: {len(data['decayed'])}")
