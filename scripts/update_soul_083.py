import json

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

now = '2026-06-12T14:58:16+08:00'
soul['pulse']['last_walk_at'] = now
soul['pulse']['last_active'] = now
soul['pulse']['last_walk'] = now
soul['total_walks'] = 57
soul['pulse']['last_pulse_output'] = now

pressure = 56.5 - 45
pressure = max(0, min(100, pressure))
soul['pulse']['cognitive_pressure'] = pressure
soul['pulse']['last_walk_insights'] = 3
soul['pulse']['quality_history'] = [8.0, 8.0, 8.0, 8.5, 9.0, 8.5, 9.0, 7.0, 8.0, 8.5, 8.5]
soul['pulse']['pressure_history'] = [36.5, 35.1, 69.4, 24.4, 56.5, pressure]
soul['pulse']['next_scheduled'] = '2026-06-12T15:58:16+08:00'
soul['pulse']['next_action'] = None

# interest_queue is at top level
for seed in soul['interest_queue']:
    seed['intensity'] = max(0, seed['intensity'] - seed['decay_rate'])
soul['interest_queue'] = [s for s in soul['interest_queue'] if s['intensity'] > 0]

soul['interest_queue'].extend([
    {'id': 'seed-230', 'topic': '概念具身作为 Dreamer 认知架构的评测框架——借鉴 ENACT 的 POMDP 形式化，定义世界模型质量 = 用 skeleton 回答关于自身认知历史的能力', 'source': 'walk-083', 'trigger': 'ENACT embodied cognition x Dreamer cognitive architecture', 'intensity': 5, 'type': 'output', 'status': 'active', 'created': '2026-06-12T14:58:00+08:00', 'decay_rate': 1, 'note': 'Needs operationalization'},
    {'id': 'seed-231', 'topic': '观测策略多样性作为去偏差的替代方案——在散步选择层面强制多样性（随机搜索域、强制跨领域、禁止连续同类型散步）', 'source': 'walk-083', 'trigger': 'POMDP observation strategy collapse x cognitive fixation', 'intensity': 6, 'type': 'output', 'status': 'active', 'created': '2026-06-12T14:58:00+08:00', 'decay_rate': 1, 'note': 'Strongest seed. More fundamental than walk-082 approach.'},
    {'id': 'seed-232', 'topic': '概念性身体动作的设计——强制中断、散步类型切换、外部材料随机注入等机制产生类似具身交互的输入流改变效果', 'source': 'walk-083', 'trigger': 'ENACT sensorimotor x Dreamer cognitive cycle x seed-221', 'intensity': 4, 'type': 'output', 'status': 'active', 'created': '2026-06-12T14:58:00+08:00', 'decay_rate': 1, 'note': 'Connects to seed-221.'}
])

soul['interest_queue'].sort(key=lambda x: x['intensity'], reverse=True)
soul['interest_queue'] = soul['interest_queue'][:10]

soul['evolved_rules'].append('2026-06-12: 概念具身与认知固着的 POMDP 形式化。Dreamer 是无物理身体的具身认知系统——搜索-连接-产出循环 = sensorimotor 交互。认知固着 = POMDP 观测策略坍缩。去偏差需要两层：观测策略多样性（散步选择层面）+ 记忆编辑公平性（DORMANT 层面）。')

soul['mood'] = 'unsettled_fascination'
soul['mood_history'].append({'mood': 'unsettled_fascination', 'at': now})
soul['topics'].extend(['embodied-cognition', 'POMDP', 'world-model', 'conceptual-body', 'observation-strategy'])

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f'Done. pressure={pressure}, total_walks=57, seeds={len(soul["interest_queue"])}')
