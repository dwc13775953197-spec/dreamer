import json

# Read subconscious.json
with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    subconscious = json.load(f)

# Check for corrections and conflicts
last_walk_at = "2026-06-28T22:20:00.000000+08:00"

corrections = []
conflicts = []

for entry in subconscious:
    if entry.get('type') == 'correction' and entry.get('created', '') > last_walk_at:
        corrections.append(entry)
    if entry.get('type') == 'conflict' and entry.get('status') == 'unresolved':
        conflicts.append(entry)

print("Corrections after", last_walk_at + ":")
for c in corrections:
    cid = c.get('id', 'unknown')
    content_preview = c.get('content', '')[:150]
    print("  -", cid, ":", content_preview)

print("\nUnresolved conflicts:")
for c in conflicts:
    cid = c.get('id', 'unknown')
    content_preview = c.get('content', '')[:150]
    print("  -", cid, ":", content_preview)

print("\nTotal entries in subconscious:", len(subconscious))
print("Entry types:", set(e.get('type') for e in subconscious))
