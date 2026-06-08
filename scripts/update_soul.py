import json, datetime

now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
now_str = now.isoformat()

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    s = json.load(f)

# Update pulse
s['pulse']['last_walk_at'] = now_str
s['pulse']['last_walk'] = now_str
s['pulse']['total_walks'] = 44
s['pulse']['last_pulse_output'] = now_str

# Pressure update: was 53.92, subtract release for new insights
pressure = 53.92
pressure -= 4 * s['pulse']['pressure_params']['release_per_insight']  # 4 new insights
pressure = max(0, min(100, pressure))
s['pulse']['cognitive_pressure'] = round(pressure, 2)

# Quality history
s['pulse']['quality_history'].append(8.1)
s['pulse']['quality_history'] = s['pulse']['quality_history'][-10:]
s['pulse']['last_walk_insights'] = 4

# Update affect
s['affect']['primary'] = 'wistful_recognition'
s['affect']['intensity'] = 0.65
s['affect']['valence'] = 0.45
s['affect']['arousal'] = 0.50

# Add mood
s['mood_history'].append({"mood": "wistful_recognition", "at": now_str})

# Add new seeds to interest_queue
new_seeds = [
    {
        "id": "seed-140",
        "topic": "记忆巩固的情绪标记：REM 阶段的跨领域整合能否引入情感优先级？",
        "source": "walk-049",
        "trigger": "海马体 REM 期间杏仁核调节跨领域连接",
        "intensity": 4,
        "type": "output",
        "status": "active",
        "created": now_str,
        "decay_rate": 1,
        "note": "高情感强度的条目在 REM 中优先组合"
    },
    {
        "id": "seed-141",
        "topic": "意图性睡眠：DORMANT 的主动回放 vs 海马体的被动回放，哪个更真实？",
        "source": "walk-049",
        "trigger": "叙事完整性检查的盲点",
        "intensity": 3,
        "type": "output",
        "status": "active",
        "created": now_str,
        "decay_rate": 1,
        "note": "选择 = 偏见？主动选择的意外发现缺失"
    },
    {
        "id": "seed-142",
        "topic": "突触修剪的主动吞噬：subconscious 衰减系统能否从被动衰减升级为主动识别+移除？",
        "source": "walk-049",
        "trigger": "小胶质细胞介导的突触修剪",
        "intensity": 4,
        "type": "output",
        "status": "active",
        "created": now_str,
        "decay_rate": 1,
        "note": "小胶质细胞 = 主动吞噬 vs 被动衰减"
    }
]

s['interest_queue'].extend(new_seeds)

# Queue maintenance: decay all, remove <= 0, keep max 15
for seed in s['interest_queue']:
    seed['intensity'] = max(0, seed['intensity'] - seed.get('decay_rate', 1))
s['interest_queue'] = [s2 for s2 in s['interest_queue'] if s2['intensity'] > 0]
s['interest_queue'].sort(key=lambda x: x['intensity'], reverse=True)
s['interest_queue'] = s['interest_queue'][:15]

# Update energy (slight decrease from walk)
s['energy'] = 38

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(s, f, indent=2, ensure_ascii=False)

print("soul.json updated successfully")
print(f"New pressure: {s['pulse']['cognitive_pressure']}")
print(f"Total walks: {s['pulse']['total_walks']}")
print(f"Interest queue length: {len(s['interest_queue'])}")
