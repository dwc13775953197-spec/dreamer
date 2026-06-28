import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    data = json.load(f)

last_walk_time = "2026-06-28T11:50:43"
corrections = [e for e in data if e.get('type') == 'correction' and e.get('created', '') > last_walk_time]
conflicts = [e for e in data if e.get('type') == 'conflict' and e.get('status') == 'unresolved']

print("=== CORRECTIONS ===")
for c in corrections:
    print(json.dumps(c, ensure_ascii=False, indent=2)[:500])
    print("---")

print("\n=== UNRESOLVED CONFLICTS ===")
for c in conflicts:
    print(json.dumps(c, ensure_ascii=False, indent=2)[:500])
    print("---")

# Check for diversity seeds
diversity_seeds = [e for e in data if 'diversity' in e.get('id', '') or e.get('type') == 'diversity_seed']
print("\n=== DIVERSITY SEEDS ===")
for s in diversity_seeds:
    print(f"  {s.get('id')}: {s.get('content', '')[:100]}")

print("\n=== SEED-TYPE ENTRIES ===")
seeds = [e for e in data if e.get('type') in ('seed', 'diversity_seed')]
for s in seeds[:10]:
    print(f"  {s.get('id')}: type={s.get('type')}, content={s.get('content', '')[:80]}")
