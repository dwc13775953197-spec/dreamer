import json
from datetime import datetime, timezone, timedelta

# Read current time and state
current_time = datetime(2026, 6, 29, 4, 16, 10, tzinfo=timezone(timedelta(hours=8)))
last_walk_time = datetime(2026, 6, 29, 3, 43, 32, tzinfo=timezone(timedelta(hours=8)))

# Calculate hours since last walk
minutes_since_last = (current_time - last_walk_time).total_seconds() / 60
hours_since_last = minutes_since_last / 60

print(f"Minutes since last walk: {minutes_since_last:.1f}")
print(f"Hours since last walk: {hours_since_last:.3f}")

# Read soul.json
with open('/home/dwc1377/hermes_dreamer/soul.json', 'r') as f:
    soul = json.load(f)

# Update pressure
base_rate = soul['pulse']['pressure_params']['base_rate']
time_factor = soul['pulse']['pressure_params']['time_factor']
interval_minutes = soul['pulse']['current_interval_min']

pressure = soul['pulse']['pressure']
print(f"Current pressure: {pressure}")

# Update pressure
pressure += base_rate * interval_minutes
pressure += hours_since_last * time_factor
print(f"Pressure after update (before clamp): {pressure}")
pressure = min(pressure, 100.0)
print(f"Pressure after clamp: {pressure}")

# Update next_scheduled (pressure > 70 → interval = 15 min)
interval = 15
next_scheduled = current_time + timedelta(minutes=interval)
print(f"Next scheduled: {next_scheduled.isoformat()}")

# Update soul.json
soul['pulse']['pressure'] = pressure
soul['pulse']['next_scheduled'] = next_scheduled.isoformat()
soul['pulse']['last_pulse_output'] = current_time.isoformat()

# Write back
with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, indent=2, ensure_ascii=False)

print("\nsoul.json updated successfully")
print(f"\nSummary:")
print(f"  State: ACTIVE (no walk triggered)")
print(f"  Reason: cognitive_pressure ({pressure}) < effective_threshold (105, due to energy < 30)")
print(f"  Energy: 28 (low)")
print(f"  Pressure: {pressure}")
print(f"  Next check: {next_scheduled.strftime('%H:%M')}")
