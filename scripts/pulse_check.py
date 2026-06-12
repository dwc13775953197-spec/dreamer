import json, math
from datetime import datetime, timezone, timedelta

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)
with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

p = soul['pulse']
now = datetime.now(timezone(timedelta(hours=8)))
last_walk = datetime.fromisoformat(p['last_walk_at'].replace('+0800', '+08:00'))
hours_since = (now - last_walk).total_seconds() / 3600

print(f"Hours since last walk: {hours_since:.1f}")
print(f"Current pressure: {p['cognitive_pressure']}")
print(f"Threshold: {p['pressure_threshold']}")
print(f"Energy: {soul['energy']}")

base_rate = p['pressure_params']['base_rate']
time_factor = p['pressure_params']['time_factor']
interval = 30

pressure = p['cognitive_pressure']
pressure += base_rate * (interval / 60)
pressure += hours_since * time_factor * 0.1

has_diversity = any(e['type'] == 'diversity_seed' and e['status'] == 'active' for e in sub['entries'])
if has_diversity:
    pressure += 15
    print("Diversity seed found: +15 pressure")

pressure = max(0, min(100, pressure))
print(f"Updated pressure: {pressure:.1f}")

curiosity = p['modifiers']['curiosity_factor']
energy = soul['energy']
threshold = p['pressure_threshold']

if energy < 30:
    eff_threshold = threshold * 1.5
elif curiosity > 0.9:
    eff_threshold = threshold * 0.7
else:
    eff_threshold = threshold

print(f"Effective threshold: {eff_threshold:.1f}")
print(f"Should walk: {pressure >= eff_threshold}")

if pressure > 70:
    next_interval = 15
elif pressure < 20:
    next_interval = 60
elif energy < 20:
    next_interval = 90
else:
    next_interval = 30

print(f"Next interval: {next_interval} minutes")

print("\n--- Subconscious Decay ---")
for entry in sub['entries']:
    if entry['status'] in ('decayed', 'consumed'):
        continue
    old = entry['strength']
    entry['strength'] = max(0, old - entry.get('decay_rate', 1) * 0.5)
    if entry['strength'] < 3:
        entry['status'] = 'decayed'
    print(f"  {entry['id']}: {old:.2f} -> {entry['strength']:.2f} ({entry['status']})")

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, ensure_ascii=False, indent=2)

p['cognitive_pressure'] = round(pressure, 1)
p['pressure_history'].append(round(pressure, 1))
p['pressure_history'] = p['pressure_history'][-20:]

next_time = now + timedelta(minutes=next_interval)
p['next_scheduled'] = next_time.isoformat()

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f"\nNext scheduled: {p['next_scheduled']}")
print("State updated.")
