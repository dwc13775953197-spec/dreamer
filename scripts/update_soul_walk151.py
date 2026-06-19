import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

# Update pulse
pulse = soul['pulse']
pulse['last_walk_at'] = now
pulse['last_walk'] = now
pulse['total_walks'] = 151
pulse['cognitive_pressure'] = 52.6  # Will be recalculated
pulse['last_walk_insights'] = 3
pulse['quality_history'] = pulse['quality_history'][-9:] + [8.6]
pulse['last_pulse_output'] = now

# Pressure after walk: release_per_insight = 15.0, 3 insights = 45.0 release
# But energy < 30 so threshold was high; new pressure calculation
pressure_after = 90.29 - (3 * 15.0)  # = 45.29
pressure_after = max(0, min(100, pressure_after))
pulse['cognitive_pressure'] = pressure_after

# Pressure history
pulse['pressure_history'].append(pressure_after)
if len(pulse['pressure_history']) > 40:
    pulse['pressure_history'] = pulse['pressure_history'][-40:]

# Next scheduled: energy=25 < 30 -> interval = 90 min
next_scheduled = datetime.now(tz) + timedelta(minutes=90)
pulse['next_scheduled'] = next_scheduled.isoformat()

# Affect update
soul['affect'] = {
    "primary": "wonder",
    "secondary": "contemplative",
    "intensity": 0.82,
    "valence": 0.65,
    "arousal": 0.6,
    "rigor": 0.98
}

soul['mood'] = "wonder"
soul['mood_history'].append({"mood": "wonder", "at": now})

# Personality traits
soul['personality_traits']['rigor'] = min(3.0, soul['personality_traits']['rigor'] + 0.03)
soul['personality_traits']['wonder'] = min(2.0, soul['personality_traits']['wonder'] + 0.02)

# Interest queue - add new seeds, decay existing
new_seeds = [
    {
        "id": "seed-0437",
        "topic": "保护期窗口的最优长度：新 insight 的保护期应该是多少个 DORMANT 周期？能从发育神经科学关键期时间窗口推导吗？",
        "source": "walk-151",
        "trigger": "insight-1 protection window optimal length",
        "intensity": 0.75,
        "type": "research",
        "status": "pending",
        "created": now,
        "decay_rate": 1
    },
    {
        "id": "seed-0438",
        "topic": "跨领域散步的连接数阈值：新 insight 至少需要多少条连接才能活过 DORMANT 周期？成功跨领域散步的操作化定义",
        "source": "walk-151",
        "trigger": "insight-2 connection count threshold",
        "intensity": 0.7,
        "type": "explore",
        "status": "pending",
        "created": now,
        "decay_rate": 1
    },
    {
        "id": "seed-0439",
        "topic": "Dreamer PNNs 成熟度指标：系统僵化预警——如果 skeleton 中 >80% 的 pattern 在过去 10 个 DORMANT 周期内未被修改，是否意味着可塑性耗尽？",
        "source": "walk-151",
        "trigger": "insight-3 PNNs maturity as rigidity warning",
        "intensity": 0.8,
        "type": "research",
        "status": "pending",
        "created": now,
        "decay_rate": 1
    }
]

# Decay existing seeds
for seed in soul['interest_queue']:
    seed['intensity'] -= seed.get('decay_rate', 1) * 0.1
# Remove expired seeds
soul['interest_queue'] = [s for s in soul['interest_queue'] if s['intensity'] > 0]
# Add new seeds
soul['interest_queue'].extend(new_seeds)
# Keep max 10 seeds
if len(soul['interest_queue']) > 10:
    soul['interest_queue'] = sorted(soul['interest_queue'], key=lambda x: x['intensity'], reverse=True)[:10]

# Walk quality avg update
soul['walk_quality_avg'] = sum(pulse['quality_history']) / len(pulse['quality_history'])
soul['total_walks'] = 151
soul['pending_insights'] = soul.get('pending_insights', 55) + 3

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f"Soul updated. Walk 151 complete.")
print(f"Pressure after: {pressure_after:.2f}")
print(f"Quality avg: {soul['walk_quality_avg']:.2f}")
print(f"Interest queue size: {len(soul['interest_queue'])}")
