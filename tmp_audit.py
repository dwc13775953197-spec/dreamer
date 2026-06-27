import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    data = json.load(f)

corrections = [e for e in data if e.get('type') == 'correction']
conflicts = [e for e in data if e.get('type') == 'conflict' and e.get('status') == 'unresolved']
seeds = [e for e in data if 'seed' in e.get('type', '') or 'diversity' in str(e.get('id', ''))]

print(f'Total entries: {len(data)}')
print(f'Corrections: {len(corrections)}')
print(f'Unresolved conflicts: {len(conflicts)}')
print(f'Diversity seeds: {len(seeds)}')

for c in corrections:
    print(f'  CORRECTION id={c.get("id")}')

for c in conflicts:
    print(f'  CONFLICT id={c.get("id")}')

for s in seeds:
    print(f'  SEED id={s.get("id")}')
