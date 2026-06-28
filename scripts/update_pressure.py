import json
from datetime import datetime, timedelta, timezone

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)
now_iso = now.isoformat()

with open('/home/dwc1377/hermes_dreamer/soul.json', 'r') as f:
    soul = json.load(f)

pulse = soul['pulse']

# Step 2: Pressure was 100, effective_threshold = 112.5 (energy < 30)
# 100 < 112.5 → NO WALK

# Step 3: Update pressure (even without walk)
last_walk_at = datetime.fromisoformat(pulse['last_walk_at'])
interval_minutes = pulse.get('current_interval_min', 30.0)
hours_since_walk = (now - last_walk_at).total_seconds() / 3600.0

base_rate = pulse['pressure_params']['base_rate']
time_factor = pulse['pressure_params']['time_factor']
new_pressure = pulse['pressure'] + (base_rate * interval_minutes) + (hours_since_walk *time_factor)
new_pressure = max(0.0, min(100.0, new_pressure))

pulse['pressure'] = new_pressure
pulse['cognitive_pressure'] = new_pressure

# Step 5: Calculate next check interval
if new_pressure > 70:
    next_interval = 15
elif new_pressure < 20:
    next_interval = 60
elif soul['energy'] < 20:
    next_interval = 90
else:
    next_interval = 30  # fallback

pulse['current_interval_min'] = next_interval
pulse['next_scheduled'] = (now + timedelta(minutes=next_interval)).isoformat()
pulse['last_active'] = now_iso

# Append to pressure_history
pulse['pressure_history'].append(new_pressure)
pulse['quality_history'].append(0.0)  # no walk = quality 0, or should we not append?
# Actually, quality_history should only track actual walks. Let me not append.

print(f"Updated soul.json:")
print(f"  pressure: {new_pressure:.2f}")
print(f"  next_interval: {next_interval} min")
print(f"  next_scheduled: {pulse['next_scheduled']}")
print(f"  hours_since_walk: {hours_since_walk:.2f}")

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print("\nSaved!")
