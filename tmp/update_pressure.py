import json
from datetime import datetime, timezone, timedelta

# Read soul.json
with open('/home/dwc1377/hermes_dreamer/soul.json', 'r') as f:
    soul = json.load(f)

# Current time
now = datetime(2026, 6, 29, 0, 14, 6, tzinfo=timezone(timedelta(hours=8)))

# Pressure calculation
cognitive_pressure = soul['pulse']['cognitive_pressure']
pressure_threshold = soul['pulse']['pressure_threshold']
energy = soul['energy']
curiosity = soul['pulse']['modifiers']['curiosity_factor']

# Effective threshold
if energy < 30:
    effective_threshold = pressure_threshold * 1.5
elif curiosity > 0.9:
    effective_threshold = pressure_threshold * 0.7
else:
    effective_threshold = pressure_threshold

print(f"Energy: {energy}")
print(f"Curiosity: {curiosity}")
print(f"Raw threshold: {pressure_threshold}")
print(f"Effective threshold: {effective_threshold}")
print(f"Cognitive pressure: {cognitive_pressure}")
print(f"Walk triggered: {cognitive_pressure >= effective_threshold}")

# Time since last pulse (last_active)
last_active = datetime.fromisoformat(soul['pulse']['last_active'])
interval_minutes = (now - last_active).total_seconds() / 60.0
print(f"\nLast active: {soul['pulse']['last_active']}")
print(f"Interval minutes: {interval_minutes:.1f}")

# Time since last walk
last_walk_at = datetime.fromisoformat(soul['pulse']['last_walk_at'])
hours_since_last_walk = (now - last_walk_at).total_seconds() / 3600.0
print(f"Last walk: {soul['pulse']['last_walk_at']}")
print(f"Hours since last walk: {hours_since_last_walk:.2f}")

# Pressure update
pp = soul['pulse']['pressure_params']
pressure = cognitive_pressure
pressure += pp['base_rate'] * interval_minutes
pressure += hours_since_last_walk * pp['time_factor']
# Check for diversity_seed in subconscious.json
# (skipped - need to read separately)

pressure = max(0.0, min(100.0, pressure))
print(f"\nPressure after update: {pressure:.2f}")

# Next interval calculation
current_interval = soul['pulse'].get('current_interval_min', 30.0)
if pressure > 70:
    next_interval = 15.0
elif pressure < 20:
    next_interval = 60.0
else:
    next_interval = 30.0

if energy < 20:
    next_interval = max(next_interval, 90.0)

print(f"Next interval: {next_interval} minutes")

# Next scheduled
next_scheduled = now + timedelta(minutes=next_interval)
print(f"Next scheduled: {next_scheduled.isoformat()}")

# Quality history (unchanged - no walk)
quality_history = soul['pulse'].get('quality_history', [])

# Write updated soul.json
soul['pulse']['cognitive_pressure'] = pressure
soul['pulse']['pressure'] = pressure
soul['pulse']['next_scheduled'] = next_scheduled.isoformat()
soul['pulse']['current_interval_min'] = next_interval
soul['pulse']['last_active'] = now.isoformat()
soul['pressure'] = pressure
soul['cognitive_pressure'] = pressure
soul['next_scheduled'] = next_scheduled.isoformat()
# Update pressure_history
ph = soul['pulse'].get('pressure_history', [])
if len(ph) >= 10:
    ph = ph[-9:]
ph.append(pressure)
soul['pulse']['pressure_history'] = ph
soul['pulse']['quality_history'] = quality_history

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print("\nsoul.json updated successfully")
