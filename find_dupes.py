import json
from datetime import datetime, timezone, timedelta

# Read raw file
with open('/home/dwc1377/hermes_dreamer/soul.json', 'r') as f:
    content = f.read()

lines = content.split('\n')

# Find duplicate keys at all levels
# Track depth by braces
depth = 0
root_keys = {}
current_path = []

for i, line in enumerate(lines):
    stripped = line.strip()
    
    # Count opening braces
    open_count = stripped.count('{')
    close_count = stripped.count('}')
    
    # Simple approach: just look for key-value patterns at root depth
    # Root depth = 1 (inside the outermost braces)
    if depth == 1 and ':' in stripped and stripped.startswith('"'):
        key_part = stripped.split(':')[0].strip()
        if key_part.startswith('"') and key_part.endswith('"'):
            key = key_part[1:-1]
            if key not in root_keys:
                root_keys[key] = []
            root_keys[key].append((i + 1, line.rstrip()))
    
    depth += open_count - close_count

print("=== DUPLICATE KEYS AT ROOT LEVEL ===")
for key, occurrences in sorted(root_keys.items()):
    if len(occurrences) > 1:
        print(f"\n  {key}:")
        for line_num, line_text in occurrences:
            print(f"    line {line_num}: {line_text[:80]}")
