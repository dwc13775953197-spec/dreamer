import json

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

pulse = soul['pulse']
pulse['last_walk_at'] = '2026-06-16T21:30:00+08:00'
pulse['last_active'] = '2026-06-16T21:30:00+08:00'
pulse['last_pulse_output'] = '2026-06-16T21:30:00+08:00'
pulse['total_walks'] = 72
soul['total_walks'] = 71

# 更新情感
soul['affect']['primary'] = 'wonder'
soul['affect']['intensity'] = 0.68
soul['mood'] = 'wonder'
soul['mood_history'].append({
    'mood': 'wonder',
    'at': '2026-06-16T21:30:00+08:00'
})

# 人格微调
soul['personality_traits']['rigor'] = min(2.0, soul['personality_traits']['rigor'] + 0.03)
soul['personality_traits']['curiosity'] = min(2.0, soul['personality_traits']['curiosity'] + 0.02)

# 压力更新
pulse['cognitive_pressure'] = max(0, pulse['cognitive_pressure'] - 3 * pulse['pressure_params']['release_per_insight'])
pulse['quality_history'].append(8.5)
pulse['quality_history'] = pulse['quality_history'][-10:]
pulse['last_walk_insights'] = 3
pulse['pressure_history'].append(pulse['cognitive_pressure'])

# 兴趣队列：衰减 + 添加新种子
decay_rate = 1
for seed in soul['interest_queue']:
    seed['intensity'] -= decay_rate / 10  # 缓慢衰减

# 移除过低的
soul['interest_queue'] = [s for s in soul['interest_queue'] if s['intensity'] > 0.3]

# 添加新种子
new_seeds = [
    {
        'id': 'seed-330',
        'topic': 'Walk Initializer 作为 Dreamer 新子流程：从 Harness 设计模式到散步的标准化入职流程',
        'source': 'walk-114',
        'trigger': 'Harness Initializer Agent 映射到 Dreamer',
        'intensity': 0.65,
        'type': 'research',
        'status': 'pending',
        'created': '2026-06-16T21:30:00+08:00',
        'decay_rate': 1
    },
    {
        'id': 'seed-331',
        'topic': '"可合并状态"作为散步结束不变量：如何定义和检测？',
        'source': 'walk-114',
        'trigger': 'Harness clean state 映射',
        'intensity': 0.59,
        'type': 'research',
        'status': 'pending',
        'created': '2026-06-16T21:30:00+08:00',
        'decay_rate': 1
    },
    {
        'id': 'seed-332',
        'topic': '格式约束即认知约束：frontmatter 的结构化如何影响散步产出质量？',
        'source': 'walk-114',
        'trigger': 'JSON vs Markdown 选择',
        'intensity': 0.49,
        'type': 'research',
        'status': 'pending',
        'created': '2026-06-16T21:30:00+08:00',
        'decay_rate': 1
    }
]

soul['interest_queue'].extend(new_seeds)

# 如果超过 15 个，淘汰最低的
if len(soul['interest_queue']) > 15:
    soul['interest_queue'].sort(key=lambda s: s['intensity'])
    soul['interest_queue'] = soul['interest_queue'][-15:]

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f'Updated soul.json. Walks: {pulse["total_walks"]}, Pressure: {pulse["cognitive_pressure"]:.1f}, Queue: {len(soul["interest_queue"])}')
