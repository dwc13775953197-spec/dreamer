#!/usr/bin/env python3
import json
from datetime import datetime, timezone, timedelta

# Read current state
with open('/home/dwc1377/hermes_dreamer/soul.json', 'r') as f:
    state = json.load(f)

# Current time
tz = timezone(timedelta(hours=8))
now = datetime(2026, 6, 27, 7, 35, 44, tzinfo=tz)

# Last walk time from file system (walk-247: 2026-06-27 05:38)
last_walk_at = datetime(2026, 6, 27, 5, 38, 0, tzinfo=tz)
hours_since_last_walk = (now - last_walk_at).total_seconds() / 3600.0

# Pressure calculation
pulse = state['pulse']
base_rate = pulse['pressure_params']['base_rate']  # 0.5
time_factor = pulse['pressure_params']['time_factor']  # 2.0
current_interval_min = pulse['current_interval_min']  # 15

pressure = pulse.get('cognitive_pressure', pulse.get('pressure', 39.31))
pressure += base_rate * current_interval_min  # 0.5 * 15 = 7.5
pressure += hours_since_last_walk * time_factor  # ~1.95 * 2 = 3.9

# Check for diversity_seed (already confirmed none exists)
# pressure stays as is

pressure = max(0, min(100, pressure))

# Threshold dynamic adjustment
energy = state['energy']  # 22
threshold = pulse['pressure_threshold']  # 55.0
if energy < 30:
    effective_threshold = threshold * 1.5  # 82.5
else:
    effective_threshold = threshold

print(f"Hours since last walk: {hours_since_last_walk:.2f}")
print(f"Updated pressure: {pressure:.2f}")
print(f"Energy: {energy}")
print(f"Effective threshold: {effective_threshold:.2f}")
print(f"Should walk: {pressure >= effective_threshold}")

# Decision: pressure < effective_threshold → skip walk
# Interval calculation
if pressure > 70:
    interval_min = 15
elif pressure < 20:
    interval_min = 60
elif energy < 20:
    interval_min = 90
else:
    interval_min = 30

next_scheduled = now + timedelta(minutes=interval_min)
last_pulse_output = now

# Update state
pulse['cognitive_pressure'] = pressure
pulse['pressure'] = pressure  # keep in sync
pulse['next_scheduled'] = next_scheduled.isoformat()
pulse['last_pulse_output'] = last_pulse_output.isoformat()
pulse['last_active'] = now.isoformat()

# Update pressure_history (keep last 15)
pulse['pressure_history'].append(pressure)
if len(pulse['pressure_history']) > 15:
    pulse['pressure_history'] = pulse['pressure_history'][-15:]

# Decay interest queue seeds
iq = pulse.get('interest_queue', [])
for seed in iq:
    seed['intensity'] -= seed.get('decay_rate', 0.05)
# Remove expired seeds
iq = [s for s in iq if s['intensity'] > 0]
# If more than 10, remove lowest
if len(iq) > 10:
    iq.sort(key=lambda x: x['intensity'])
    iq = iq[-10:]
pulse['interest_queue'] = iq

# Update root level interest_queue too
root_iq = state.get('interest_queue', [])
for seed in root_iq:
    seed['intensity'] -= seed.get('decay_rate', 0.05)
root_iq = [s for s in root_iq if s['intensity'] > 0]
if len(root_iq) > 10:
    root_iq.sort(key=lambda x: x['intensity'])
    root_iq = root_iq[-10:]
state['interest_queue'] = root_iq

# Write updated state
with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(state, f, indent=2, ensure_ascii=False)

print(f"\nNext scheduled: {next_scheduled.isoformat()}")
print(f"Interval: {interval_min} minutes")
print(f"Remaining seeds in pulse queue: {len(iq)}")
print(f"Remaining seeds in root queue: {len(root_iq)}")
print("State updated. Skipping walk (pressure below threshold).")
