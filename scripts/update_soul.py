import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    s = json.load(f)

# Update pulse
s['pulse']['last_walk_at'] = now.isoformat()
s['pulse']['total_walks'] = 77
s['pulse']['last_walk'] = now.isoformat()
s['pulse']['last_active'] = now.isoformat()

# Pressure: was 91.90, release 3 insights x 15 = 45, new = 91.90 - 45 = 46.90
new_pressure = max(0, 91.90 - 3 * 15.0)
s['pulse']['cognitive_pressure'] = new_pressure
s['pulse']['pressure_history'].append(new_pressure)
s['pulse']['quality_history'].append(8.5)
# Keep only last 10
s['pulse']['quality_history'] = s['pulse']['quality_history'][-10:]
s['pulse']['last_walk_insights'] = 3

# Next scheduled: pressure < 20 -> 60 min interval
s['pulse']['next_scheduled'] = (now + timedelta(minutes=60)).isoformat()

# Update affect
s['affect']['primary'] = 'wonder'
s['affect']['secondary'] = 'contemplative'
s['affect']['intensity'] = 0.7

# Update energy (walk costs energy)
s['energy'] = max(20, 41 - 5)

# Add mood
s['mood_history'].append({'mood': 'wonder', 'at': now.isoformat()})

# Update interest_queue: add 3 new seeds, decay existing
new_seeds = [
    {'id': 'seed-345', 'topic': '认知成熟度指标：如何衡量一个想法是否准备好被散步加工？', 'source': 'walk-119', 'trigger': '发现 1', 'intensity': 0.55, 'type': 'research', 'status': 'pending', 'created': now.isoformat(), 'decay_rate': 1},
    {'id': 'seed-346', 'topic': '呼吸散步实验：不产出洞察的散步是否能提升后续散步的质量？', 'source': 'walk-119', 'trigger': '发现 2', 'intensity': 0.50, 'type': 'research', 'status': 'pending', 'created': now.isoformat(), 'decay_rate': 1},
    {'id': 'seed-347', 'topic': '三维认知预算的操作化：产出×模糊×延迟的平衡方程应该如何设计？', 'source': 'walk-119', 'trigger': '发现 3', 'intensity': 0.45, 'type': 'research', 'status': 'pending', 'created': now.isoformat(), 'decay_rate': 1}
]

# Decay existing seeds
for seed in s['interest_queue']:
    seed['intensity'] = max(0, seed['intensity'] - seed['decay_rate'] * 0.05)

# Remove expired seeds
s['interest_queue'] = [s for s in s['interest_queue'] if s['intensity'] > 0]

# Add new seeds
s['interest_queue'].extend(new_seeds)

# Keep max 20
if len(s['interest_queue']) > 20:
    s['interest_queue'] = sorted(s['interest_queue'], key=lambda x: x['intensity'], reverse=True)[:20]

# Add evolved rule
s['evolved_rules'].append(f'{now.strftime("%Y-%m-%d")}: 延迟是认知功能而非认知缺陷。主动拖延研究证明策略性延迟提升创造力。Dreamer 的 35 分钟壁垒 = 负能力的物理度量（系统能在输出前维持模糊的时间窗口）。三维认知预算：产出×模糊×延迟。呼吸散步 = 不产出洞察的第四种散步类型。walk-119 验证了跨散步连接（负能力+矛盾引擎+认知预算→认知延迟）的高产出模式。')

# Update stats
s['total_walks'] = s.get('total_walks', 71) + 1

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(s, f, ensure_ascii=False, indent=2)

print(f'Soul updated. Walk #{s["total_walks"]}, pressure now: {new_pressure:.2f}')
print(f'Interest queue: {len(s["interest_queue"])} seeds')
