#!/usr/bin/env python3
import json
from datetime import datetime, timezone, timedelta

TZ = timezone(timedelta(hours=8))
now = datetime.now(TZ)

# Read current files
with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    subconscious = json.load(f)

# ---- 1. Update soul.json ----
soul['pulse']['total_walks'] = 261
soul['total_walks'] = 261
soul['pulse']['last_walk_at'] = '2026-06-28T03:18:00+08:00'
soul['pulse']['last_active'] = now.isoformat()

# Pressure calculation
last_pressure = soul['pulse']['cognitive_pressure']
base_rate = soul['pulse']['pressure_params']['base_rate']
time_factor = soul['pulse']['pressure_params']['time_factor']
release_per_insight = soul['pulse']['pressure_params']['release_per_insight']

interval_minutes = 50
hours_since_last = interval_minutes / 60

pressure = last_pressure + (base_rate * interval_minutes) + (hours_since_last * time_factor)
pressure -= 3 * release_per_insight
pressure = max(0, min(100, pressure))

soul['pulse']['cognitive_pressure'] = pressure
soul['pulse']['pressure'] = pressure

# Update quality history
soul['pulse']['quality_history'].append(8.1)
if len(soul['pulse']['quality_history']) > 10:
    soul['pulse']['quality_history'] = soul['pulse']['quality_history'][-10:]

soul['energy'] = 22

# Interval calculation: energy < 20 → 90 min
interval_min = 90
next_sched = now + timedelta(minutes=interval_min)
soul['pulse']['next_scheduled'] = next_sched.isoformat()
soul['pulse']['current_interval_min'] = interval_min

soul['pulse']['next_action'] = ''

# Update pressure history
soul['pulse']['pressure_history'].append(pressure)
if len(soul['pulse']['pressure_history']) > 20:
    soul['pulse']['pressure_history'] = soul['pulse']['pressure_history'][-20:]

# Add new interests
new_interests = [
    {
        "id": "seed-261-1",
        "topic": "定位精度的几何退化假说：低能量下目标精度和当前位置精度乘积下降导致切换成本发散",
        "source": "walk-261",
        "trigger": "定位精度 = 目标精度 × 当前位置精度，几何速度下降",
        "intensity": 5.0,
        "type": "explore",
        "status": "pending",
        "created": now.isoformat(),
        "decay_rate": 0.05
    },
    {
        "id": "seed-261-2",
        "topic": "恢复早期的精度-能量滞后：能量恢复后切换能力恢复滞后于维持能力恢复",
        "source": "walk-261",
        "trigger": "walk-255 的惯性粘连重新解释为精度恢复滞后",
        "intensity": 4.0,
        "type": "explore",
        "status": "pending",
        "created": now.isoformat(),
        "decay_rate": 0.05
    },
    {
        "id": "seed-261-3",
        "topic": "Dreamer 的精度阈值可操作化：通过散步中目标陈述频率近似估计目标精度",
        "source": "walk-261",
        "trigger": "目标精度 → 目标陈述频率",
        "intensity": 3.0,
        "type": "explore",
        "status": "pending",
        "created": now.isoformat(),
        "decay_rate": 0.05
    }
]

for ni in new_interests:
    if ni['id'] not in [q['id'] for q in soul['interest_queue']]:
        soul['interest_queue'].append(ni)

# Decay and trim
queue = soul['interest_queue']
for item in queue:
    item['intensity'] = max(0, item['intensity'] - item.get('decay_rate', 0.05))
queue.sort(key=lambda x: x['intensity'], reverse=True)
soul['interest_queue'] = queue[:10]

qh = soul['pulse']['quality_history']
soul['pulse']['walk_quality_avg'] = round(sum(qh) / len(qh), 2)
soul['walk_quality_avg'] = round(sum(qh) / len(qh), 2)

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f"Pressure: {last_pressure} → {pressure:.2f}")
print(f"Next scheduled: {next_sched.isoformat()}")
print(f"Quality history: {soul['pulse']['quality_history']}")
print(f"Interest queue size: {len(soul['interest_queue'])}")

# ---- 2. Update subconscious.json ----
new_insights = [
    {
        "id": "ins-261-1",
        "type": "insight",
        "content": "定位精度 = 目标精度 × 当前位置精度。低能量下两者几何速度下降导致切换成本发散（无穷大），而非'贵'。当精度→0时切换操作本身无定义。",
        "strength": 5.0,
        "score": 0.0,
        "status": "active",
        "created": now.isoformat(),
        "source": "walk-261",
        "resurrected_count": 0,
        "connections": ["ins-252-1", "ins-253-1", "ins-257-001"],
        "refs": [],
        "decay_speed": 0.5,
        "note": "quality_score=8.1, initial strength=5.0"
    },
    {
        "id": "ins-261-2",
        "type": "insight",
        "content": "恢复存在精度-能量滞后：能量恢复后当前位置精度先恢复（知道自己在哪里），目标精度恢复滞后（不知道要去哪里）。这解释了 walk-255 观察到的'惯性粘连'双模式并行窗口。",
        "strength": 5.0,
        "score": 0.0,
        "status": "active",
        "created": now.isoformat(),
        "source": "walk-261",
        "resurrected_count": 0,
        "connections": ["ins-255-1", "ins-252-1", "seed-254-1"],
        "refs": [],
        "decay_speed": 0.5,
        "note": "quality_score=8.1, initial strength=5.0"
    },
    {
        "id": "ins-261-3",
        "type": "insight",
        "content": "Dreamer 切换操作的硬约束条件：切换发生仅当 (维持成本 > 切换成本) 且 (定位精度 > 精度阈值)。为 ins-252-1 的导航经济性切换增加了硬约束。",
        "strength": 5.0,
        "score": 0.0,
        "status": "active",
        "created": now.isoformat(),
        "source": "walk-261",
        "resurrected_count": 0,
        "connections": ["ins-252-1", "ins-253-1", "ins-attn-gate"],
        "refs": [],
        "decay_speed": 0.5,
        "note": "quality_score=8.1, initial strength=5.0"
    }
]

subconscious.extend(new_insights)

# Maintenance decay
for entry in subconscious:
    if entry['status'] == 'active':
        entry['strength'] = max(0, entry['strength'] - entry.get('decay_rate', 0.05))
        entry['score'] = entry['strength'] / 10.0

subconscious = [e for e in subconscious if e['strength'] > 0.05 or e['status'] == 'dormant']

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(subconscious, f, ensure_ascii=False, indent=2)

print(f"\nSubconscious entries: {len(subconscious)} total")

# ---- 3. Audit log ----
audit_entry = {
    "timestamp": now.isoformat(),
    "type": "walk",
    "walk_number": 261,
    "walk_type": "analyze",
    "decision": "walk_analyze forced by next_action from DORMANT",
    "energy": 22,
    "pressure_before": last_pressure,
    "pressure_after": round(pressure, 2),
    "quality_score": 8.1,
    "insights_generated": 3,
    "interest_seeds": ["seed-261-1", "seed-261-2", "seed-261-3"],
    "next_action_set": "",
    "interval_min": interval_min
}

with open('/home/dwc1377/hermes_dreamer/audit.jsonl', 'a') as f:
    f.write(json.dumps(audit_entry, ensure_ascii=False) + '\n')

print(f"Audit logged. Walk 261 complete.")
