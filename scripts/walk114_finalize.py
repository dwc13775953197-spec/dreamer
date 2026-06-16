import json

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

# Clear next_action since walk is done
soul['pulse']['next_action'] = None

# Update next_scheduled based on pressure
pressure = soul['pulse']['cognitive_pressure']
if pressure < 20:
    interval = 60
elif pressure > 70:
    interval = 15
else:
    interval = 30

from datetime import datetime, timedelta
now = datetime.now()
next_time = now + timedelta(minutes=interval)
soul['pulse']['next_scheduled'] = next_time.strftime('%Y-%m-%dT%H:%M:%S+08:00')

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f'Next scheduled: {soul["pulse"]["next_scheduled"]} (interval: {interval}min)')
