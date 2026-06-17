import json
from datetime import datetime

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+08:00')

soul['pulse']['last_walk_at'] = now
soul['pulse']['last_active'] = now
soul['pulse']['total_walks'] = 76
soul['pulse']['last_walk'] = now

new_pressure = 81.81 - (3 * 15)
new_pressure = max(0, min(100, new_pressure))
soul['pulse']['cognitive_pressure'] = new_pressure
soul['pulse']['pressure_history'].append(new_pressure)
soul['pulse']['last_walk_insights'] = 3

soul['pulse']['quality_history'].append(8.0)
soul['pulse']['quality_history'] = soul['pulse']['quality_history'][-10:]

new_seeds = [
    {'id': 'seed-342', 'topic': '负能力作为 Dreamer 的模糊预算参数：如何操作化和测量认知模糊度？', 'source': 'walk-118', 'trigger': '发现 1', 'intensity': 0.55, 'type': 'research', 'status': 'pending', 'created': now, 'decay_rate': 1},
    {'id': 'seed-343', 'topic': '语言作为闭合偏向的输出格式：是否存在更适合表达模糊性的替代格式？', 'source': 'walk-118', 'trigger': '发现 2', 'intensity': 0.45, 'type': 'research', 'status': 'pending', 'created': now, 'decay_rate': 1},
    {'id': 'seed-344', 'topic': '散步终止式重新评估：半终止和欺骗性终止是否应该是默认的散步结束方式？', 'source': 'walk-118', 'trigger': '发现 3', 'intensity': 0.45, 'type': 'research', 'status': 'pending', 'created': now, 'decay_rate': 1},
]

for seed in soul['interest_queue']:
    seed['intensity'] = round(seed['intensity'] - seed.get('decay_rate', 1) * 0.05, 4)

soul['interest_queue'].extend(new_seeds)
soul['interest_queue'] = [s for s in soul['interest_queue'] if s['intensity'] > 0]
soul['interest_queue'].sort(key=lambda x: x['intensity'], reverse=True)
soul['interest_queue'] = soul['interest_queue'][:15]

soul['mood'] = 'contemplative'
soul['mood_history'].append({'mood': 'contemplative', 'at': now})

soul['personality_traits']['wonder'] = round(soul['personality_traits']['wonder'] + 0.02, 2)
soul['personality_traits']['rigor'] = round(soul['personality_traits']['rigor'] + 0.02, 2)

scores = soul['pulse']['quality_history']
soul['walk_quality_avg'] = round(sum(scores) / len(scores), 2)
soul['pulse']['walk_quality_avg'] = soul['walk_quality_avg']

rule_date = datetime.now().strftime('%Y-%m-%d')
soul['evolved_rules'].append(rule_date + ': 负能力作为 Dreamer 的结构性补偿机制。语言输出天然偏向闭合，散步应以半终止或欺骗性终止为默认结束方式，维持系统的最优模糊区间。模糊预算（未解决矛盾对数/已解决矛盾对数）可能是下一个系统级参数。walk-118 验证了 Twist 散步对抗闭合偏向的高价值。')

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print('soul.json updated: pressure=' + str(new_pressure) + ', total_walks=76, seeds=' + str(len(soul['interest_queue'])))
