import json

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    d = json.load(f)

# Update pulse fields
d['pulse']['last_walk_at'] = '2026-06-15T21:16:47.406327+08:00'
d['pulse']['last_active'] = '2026-06-15T21:16:47.406327+08:00'

# Add quality to history
d['pulse']['quality_history'].append(8.0)
d['pulse']['quality_history'] = d['pulse']['quality_history'][-10:]

# Update pressure
d['pulse']['cognitive_pressure'] = 0.0
d['pulse']['last_walk_insights'] = 4

# Add new seeds to top-level interest_queue
d['interest_queue'].append({
    'id': 'seed-305',
    'topic': 'AI agent task decomposition fast repair mechanism',
    'source': 'walk-106',
    'trigger': 'failure mode 3 planning rigidity and fast channel problem',
    'intensity': 0.6,
    'type': 'research',
    'status': 'pending',
    'created': '2026-06-15T21:16:47.406327+08:00',
    'decay_rate': 1
})
d['interest_queue'].append({
    'id': 'seed-306',
    'topic': 'cognitive evolution punctuated equilibrium',
    'source': 'walk-106',
    'trigger': 'fast channel problem leads to evolutionary perspective',
    'intensity': 0.55,
    'type': 'research',
    'status': 'pending',
    'created': '2026-06-15T21:16:47.406327+08:00',
    'decay_rate': 1
})
d['interest_queue'].append({
    'id': 'seed-307',
    'topic': 'walk topic similarity autocorrelation analysis',
    'source': 'walk-106',
    'trigger': 'cascade failure observation quantitative verification',
    'intensity': 0.5,
    'type': 'research',
    'status': 'pending',
    'created': '2026-06-15T21:16:47.406327+08:00',
    'decay_rate': 1
})

# Add evolved rule
d['evolved_rules'].append('2026-06-15: Walk architecture is anti-task-decomposition design. Weakly-coupled cognitive atoms instead of strongly-coupled subtask chains. Consecutive same-type walks = cascade failure risk. Interest seed natural selection may be biased (strength != value). Breakthrough insights may need fast channel into skeleton, but speed vs quality tradeoff.')

# Update mood
d['mood'] = 'wonder'
d['affect']['primary'] = 'wonder'
d['affect']['intensity'] = 0.7

# Update personality traits
d['personality_traits']['curiosity'] = 1.08
d['personality_traits']['wonder'] = 1.07

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

print('soul.json updated')
