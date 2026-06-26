import json
from datetime import datetime, timezone, timedelta

with open('/home/dwc1377/hermes_dreamer/soul.json', 'r') as f:
    content = f.read()

# Handle duplicate keys by keeping the last occurrence
# Use a custom parser that takes the last value for duplicate keys
def parse_json_with_dupes(text):
    # Simple approach: find all key-value pairs at each level
    result = {}
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if '"version"' in line and ':' in line:
            pass  # handled separately
    # Actually, let's just do targeted replacements
    return None

# Let's just do targeted string replacements
# First, identify the key fields we need to update

lines = content.split('\n')
# Find duplicate key locations
dupes = {}
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('"') and ':' in stripped:
        key = stripped.split(':')[0].strip().strip('"')
        if key not in dupes:
            dupes[key] = []
        dupes[key].append(i + 1)  # 1-indexed

# Show all duplicate keys
for key, locations in dupes.items():
    if len(locations) > 1:
        print(f"DUPLICATE: {key} at lines {locations}")
