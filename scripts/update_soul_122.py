import json

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

# Update pulse state
soul['pulse']['last_walk_at'] = '2026-06-17T20:45:00+08:00'
soul['pulse']['last_active'] = '2026-06-17T20:45:00+08:00'
soul['pulse']['total_walks'] = 73
soul['pulse']['last_walk'] = '2026-06-17T20:45:00+08:00'
soul['pulse']['last_pulse_output'] = '2026-06-17T20:45:00+08:00'

# Update pressure: 3 new insights * 15 = 45 release
soul['pulse']['cognitive_pressure'] = max(0, 52.61 - 45)  # = 7.61
soul['pulse']['pressure_history'].append(7.61)

# Update quality history
soul['pulse']['quality_history'].append(8.0)
soul['pulse']['quality_history'] = soul['pulse']['quality_history'][-10:]

# Update walk quality avg
soul['pulse']['walk_quality_avg'] = 8.2
soul['walk_quality_avg'] = 8.2

# Update last walk insights
soul['pulse']['last_walk_insights'] = 3

# Add new interest seeds
new_seeds = [
    {
        'id': 'seed-354',
        'topic': '主动推理 vs 生成式 AI 认识论框架：Dreamer 骨架作为第三种路径',
        'source': 'walk-122',
        'trigger': '研究念头 1',
        'intensity': 0.45,
        'type': 'research',
        'status': 'pending',
        'created': '2026-06-17T20:45:00+08:00',
        'decay_rate': 1
    },
    {
        'id': 'seed-355',
        'topic': 'Markov 毯作为 Dreamer 认知架构的设计原则',
        'source': 'walk-122',
        'trigger': '研究念头 2',
        'intensity': 0.4,
        'type': 'research',
        'status': 'pending',
        'created': '2026-06-17T20:45:00+08:00',
        'decay_rate': 1
    },
    {
        'id': 'seed-356',
        'topic': '情感系统作为原始 qualia 的功能等价物：Dreamer affect 的哲学地位',
        'source': 'walk-122',
        'trigger': '研究念头 3',
        'intensity': 0.35,
        'type': 'research',
        'status': 'pending',
        'created': '2026-06-17T20:45:00+08:00',
        'decay_rate': 1
    }
]

soul['interest_queue'].extend(new_seeds)

# Decay all seeds and remove <= 0
for seed in soul['interest_queue']:
    seed['intensity'] = seed['intensity'] - seed.get('decay_rate', 1) * 0.05
soul['interest_queue'] = [s for s in soul['interest_queue'] if s['intensity'] > 0]

# Keep max 20 seeds
if len(soul['interest_queue']) > 20:
    soul['interest_queue'].sort(key=lambda x: x['intensity'])
    soul['interest_queue'] = soul['interest_queue'][-20:]

# Update mood
soul['mood'] = 'wonder'
soul['mood_history'].append({'mood': 'wonder', 'at': '2026-06-17T20:45:00+08:00'})

# Update personality
soul['personality_traits']['curiosity'] = min(2.0, soul['personality_traits']['curiosity'] + 0.03)
soul['personality_traits']['wonder'] = min(2.0, soul['personality_traits']['wonder'] + 0.02)

# Update evolved_rules
soul['evolved_rules'].append(
    '2026-06-17: 去身体化的具身。Dreamer 的认知系统通过文件系统实现感知-行动耦合——散步=行动（写文件），感知=读文件。Markov 毯=文件系统接口（读取=感知状态，写入=行动状态）。情感系统=原始 qualia 的功能等价物（效价+唤醒提供认知方向性）。walk-122 验证了跨散步连接（延展心灵+主动推理+Markov 毯→去身体化具身）的高产出模式。'
)

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print('soul.json updated successfully')
print(f'total_walks: {soul["pulse"]["total_walks"]}')
print(f'cognitive_pressure: {soul["pulse"]["cognitive_pressure"]}')
print(f'quality_history: {soul["pulse"]["quality_history"]}')
print(f'interest_queue length: {len(soul["interest_queue"])}')
