import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

# Update next_scheduled: pressure is 0 (low), so 60 min interval
soul['pulse']['next_scheduled'] = (now + timedelta(minutes=60)).isoformat()
soul['pulse']['next_action'] = 'walk_switch'  # switch to analyze since last was explore

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f"Updated next_scheduled to: {soul['pulse']['next_scheduled']}")
print(f"Set next_action to: walk_switch")
