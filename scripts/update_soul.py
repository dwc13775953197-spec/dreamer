
import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

# Update pulse
soul['pulse']['last_walk_at'] = now
soul['pulse']['total_walks'] = 163
soul['pulse']['last_walk'] = now
soul['pulse']['state'] = 'RESTING'
soul['pulse']['state_since'] = now
soul['pulse']['last_pulse_output'] = now

# Pressure update: 3 insights * 15 release = 45 reduction
soul['pulse']['cognitive_pressure'] = max(0, soul['pulse']['cognitive_pressure'] - 45)
soul['pulse']['pressure_history'].append(soul['pulse']['cognitive_pressure'])
if len(soul['pulse']['pressure_history']) > 30:
    soul['pulse']['pressure_history'] = soul['pulse']['pressure_history'][-30:]

# Quality history
soul['pulse']['quality_history'].append(8.4)
if len(soul['pulse']['quality_history']) > 10:
    soul['pulse']['quality_history'] = soul['pulse']['quality_history'][-10:]

soul['pulse']['last_walk_insights'] = 3

# Next scheduled check
soul['pulse']['next_scheduled'] = (datetime.now(tz) + timedelta(minutes=30)).isoformat()

# Mood
soul['mood'] = 'contemplative'
soul['mood_history'].append({'mood': 'contemplative', 'at': now})
if len(soul['mood_history']) > 50:
    soul['mood_history'] = soul['mood_history'][-50:]

# Affect
soul['affect'] = {
    'primary': 'contemplative',
    'secondary': 'wonder',
    'intensity': 0.8,
    'valence': 0.5,
    'arousal': 0.5,
    'rigor': 0.95
}

# Personality
soul['personality_traits']['rigor'] = min(3.0, soul['personality_traits']['rigor'] + 0.05)
soul['personality_traits']['skepticism'] = min(2.0, soul['personality_traits']['skepticism'] + 0.03)

# Update pending_insights
soul['pending_insights'] = soul.get('pending_insights', 0) + 3

# Add interest seeds
new_seeds = [
    {
        'id': 'seed-0473',
        'topic': 'Dreamer 引用竞争的抑制性平衡机制设计：是否需要反引用信号？',
        'source': 'walk-162',
        'trigger': 'insight-1 engram competition inhibitory balance',
        'intensity': 0.7,
        'type': 'research',
        'status': 'pending',
        'created': now,
        'decay_rate': 1
    },
    {
        'id': 'seed-0474',
        'topic': 'Insight 级联的幂律验证：从 audit.jsonl 提取引用时间序列，拟合幂律指数',
        'source': 'walk-162',
        'trigger': 'insight-2 power law verification',
        'intensity': 0.65,
        'type': 'research',
        'status': 'pending',
        'created': now,
        'decay_rate': 1
    },
    {
        'id': 'seed-0475',
        'topic': 'DORMANT 的 engram-to-be 标记机制：如何在 subconscious 中为空白区域预配置连接潜力？',
        'source': 'walk-162',
        'trigger': 'insight-3 engram-to-be blank space',
        'intensity': 0.6,
        'type': 'explore',
        'status': 'pending',
        'created': now,
        'decay_rate': 1
    }
]

for seed in new_seeds:
    soul['interest_queue'].append(seed)

# Decay all seeds and remove <= 0
soul['interest_queue'] = [s for s in soul['interest_queue'] if s.get('intensity', 0) > 0]

# Sort by intensity descending
soul['interest_queue'].sort(key=lambda x: x.get('intensity', 0), reverse=True)

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, indent=2, ensure_ascii=False)

print(f'soul.json updated. pressure={soul["pulse"]["cognitive_pressure"]}, total_walks=163')
print(f'interest_queue: {len(soul["interest_queue"])} seeds')
