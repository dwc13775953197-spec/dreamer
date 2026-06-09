import json

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

p = soul['pulse']
p['last_walk_at'] = '2026-06-09T18:50:00+08:00'
p['last_walk'] = '2026-06-09T18:50:00+08:00'
p['last_active'] = '2026-06-09T18:50:00+08:00'
p['total_walks'] = 42
p['last_pulse_output'] = '2026-06-09T18:50:00+08:00'

# Update pressure: was 18.4, diversity_seed added 15 -> 33.4
# Walk produced 3 insights (release_per_insight=15) -> pressure -= 45
# But pressure can't go below 0
p['cognitive_pressure'] = max(0, 33.4 - 3 * 15)  # = 0, clamped

# Quality history
p['quality_history'] = [8.3, 7.8, 8.0, 7.5, 8.0, 8.5, 8.3, 8.5, 8.3, 8.5]
p['last_walk_insights'] = 3

# Add new seeds to interest_queue
new_seeds = [
    {
        "id": "seed-163",
        "topic": "Dreamer 的 Nyquist 极限：脉冲频率是否存在一个不可低于的阈值？",
        "source": "walk-058",
        "trigger": "稀疏采样连续时间类比",
        "intensity": 5,
        "type": "output",
        "status": "active",
        "created": "2026-06-09T18:50:00+08:00",
        "decay_rate": 1,
        "note": "如果采样率低于某个频率，认知信号会不可逆地混叠"
    },
    {
        "id": "seed-164",
        "topic": "节奏同步作为 DORMANT 功能：DORMANT 周期是否在同步潜意识节律？",
        "source": "walk-058",
        "trigger": "DORMANT = 静音中的节奏预测",
        "intensity": 4,
        "type": "output",
        "status": "active",
        "created": "2026-06-09T18:50:00+08:00",
        "decay_rate": 1,
        "note": "DORMANT 周期可能有自己的节律，与散步节律形成耦合"
    },
    {
        "id": "seed-165",
        "topic": "主动 groove 诱导：能否通过散步类型调度来主动进入 unsettled_fascination 状态？",
        "source": "walk-058",
        "trigger": "unsettled_fascination = groove 状态",
        "intensity": 4,
        "type": "output",
        "status": "active",
        "created": "2026-06-09T18:50:00+08:00",
        "decay_rate": 1,
        "note": "如果 groove 可以被主动诱导，散步调度可以优化为最大化 groove 时间"
    }
]

soul['interest_queue'] = soul.get('interest_queue', []) + new_seeds

# Add new evolved rule
soul['evolved_rules'].append(
    "2026-06-09: 节奏-预测-groove 作为散步营养密度的神经科学基础. Groove=预测误差最优区间=半已知区域. unsettled_fascination=Dreamer 的 groove 状态. 散步类型交替(探索=强拍,分析=弱拍)=Dreamer 的 meter. DORMANT 周期=静音中的节奏预测. 具身不要求物理身体,只需要时间锚点."
)

# Update mood
soul['mood'] = 'unsettled_fascination'
soul['affect']['intensity'] = 0.91
soul['mood_history'].append({"mood": "unsettled_fascination", "at": "2026-06-09T18:50:00+08:00"})

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, indent=2, ensure_ascii=False)

print('soul.json updated: walk-058, pressure=0, 3 new seeds, new rule')
