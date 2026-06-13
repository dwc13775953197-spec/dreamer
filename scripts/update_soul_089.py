import json, datetime

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
now_str = now.isoformat()

pulse = soul['pulse']
pulse['last_walk_at'] = now_str
pulse['last_walk'] = now_str
pulse['total_walks'] = 59
pulse['last_pulse_output'] = now_str

new_insights = 4
new_patterns = 3
release = pulse['pressure_params']['release_per_insight']
pressure = pulse['cognitive_pressure']
pressure -= new_insights * release
pressure -= new_patterns * release * 2
pressure = max(0, min(100, pressure))
pulse['cognitive_pressure'] = round(pressure, 1)

pulse['quality_history'].append(8.5)
pulse['quality_history'] = pulse['quality_history'][-10:]
pulse['last_walk_insights'] = new_insights
pulse['pressure_history'].append(round(pressure, 1))

if pressure > 70:
    next_interval = 15
elif pressure < 20:
    next_interval = 60
elif soul['energy'] < 20:
    next_interval = 90
else:
    next_interval = 30

next_scheduled = now + datetime.timedelta(minutes=next_interval)
pulse['next_scheduled'] = next_scheduled.isoformat()
pulse['current_interval_min'] = next_interval

soul['evolved_rules'].append(
    '2026-06-13: 遗忘是拓扑的而非均匀的。Synapse 扩散激活模型：图结构中连接丰富的节点天然更耐遗忘。DORMANT 均匀衰减是需要修正的简化。三维记忆评估替代单维度 strength。DORMANT 周期间隔约等于艾宾浩斯间隔重复时间表。'
)

new_seeds = [
    {
        'id': 'seed-247',
        'topic': '记忆编码深度的自动化评估——如何区分被提到和被深度使用的 insight',
        'source': 'walk-089',
        'trigger': 'Synapse 三维记忆框架 x DORMANT 单维度 strength',
        'intensity': 0.6,
        'type': 'output',
        'status': 'active',
        'created': now_str,
        'decay_rate': 1,
        'note': 'Most actionable design improvement from this walk.'
    },
    {
        'id': 'seed-248',
        'topic': 'DORMANT 拓扑衰减模型——从均匀衰减到图结构衰减的改造方案',
        'source': 'walk-089',
        'trigger': 'Synapse spreading activation x ins-065 遗忘即选择',
        'intensity': 0.7,
        'type': 'output',
        'status': 'active',
        'created': now_str,
        'decay_rate': 1,
        'note': 'Highest intensity seed. Architectural change with large potential impact.'
    },
    {
        'id': 'seed-249',
        'topic': '情景记忆索引——为 skeleton pattern 保留起源标记的最小方案',
        'source': 'walk-089',
        'trigger': 'Synapse 情景记忆缺失 = 记忆陈旧性精确机制',
        'intensity': 0.5,
        'type': 'output',
        'status': 'active',
        'created': now_str,
        'decay_rate': 1,
        'note': 'Small addition to DORMANT: store origin metadata alongside each entry.'
    }
]

for seed in new_seeds:
    soul['interest_queue'].append(seed)

for seed in soul['interest_queue']:
    seed['intensity'] = round(seed['intensity'] - 0.1, 1)

soul['interest_queue'] = [s for s in soul['interest_queue'] if s['intensity'] > 0]

soul['affect']['primary'] = 'anticipatory_tension'
soul['affect']['intensity'] = 0.72
soul['mood'] = 'anticipatory_tension'
soul['mood_history'].append({'mood': 'anticipatory_tension', 'at': now_str})

soul['personality_traits']['rigor'] = min(1.5, soul['personality_traits']['rigor'] + 0.02)
soul['personality_traits']['curiosity'] = min(1.0, soul['personality_traits']['curiosity'] + 0.01)
soul['energy'] = max(0, soul['energy'] - 3)

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f'Pressure after walk: {pulse["cognitive_pressure"]}')
print(f'Quality history: {pulse["quality_history"]}')
print(f'Total walks: {pulse["total_walks"]}')
print(f'Interest queue length: {len(soul["interest_queue"])}')
print(f'Evolved rules count: {len(soul["evolved_rules"])}')
print(f'Energy: {soul["energy"]}')
print(f'Next scheduled: {pulse["next_scheduled"]}')
