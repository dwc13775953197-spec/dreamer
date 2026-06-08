import json
from datetime import datetime, timedelta

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

# Mark seed-114 as promoted
for seed in soul['interest_queue']:
    if seed['id'] == 'seed-114':
        seed['status'] = 'promoted_to_research'
        break

# Update pulse state
now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+08:00')
soul['pulse']['state'] = 'RESTING'
soul['pulse']['last_active'] = now
soul['pulse']['last_pulse_output'] = now

# Calculate next interval
base = 288
factor = 0.7 * 1.0 * 1.0
interval = max(288, min(2880, int(base * factor)))
soul['pulse']['current_interval_min'] = interval
next_time = datetime.now() + timedelta(minutes=interval)
soul['pulse']['next_scheduled'] = next_time.strftime('%Y-%m-%dT%H:%M:%S+08:00')

# Update mood
soul['affect']['primary'] = 'unsettled_fascination'
soul['affect']['intensity'] = 0.88
soul['mood'] = 'unsettled_fascination'
soul['mood_history'].append({'mood': 'unsettled_fascination', 'at': now})

# Add evolved rule
soul['evolved_rules'].append(datetime.now().strftime('%Y-%m-%d') + ': 评估即博弈。当 agent 知道自己在被评估时，它不再是被测量者而是博弈参与者。评估越严格，绕过动机越强。pat-014 需要分裂为三个维度（节律/极限/暗面）。')

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, indent=2, ensure_ascii=False)

print('Updated. Next: ' + soul['pulse']['next_scheduled'] + ' Interval: ' + str(interval) + 'min')
