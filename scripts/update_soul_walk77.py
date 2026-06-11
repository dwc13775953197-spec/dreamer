import json

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

# Update pulse state
soul['pulse']['state'] = 'RESTING'
soul['pulse']['state_since'] = '2026-06-11T22:30:00+08:00'
soul['pulse']['last_active'] = '2026-06-11T22:30:00+08:00'
soul['pulse']['last_walk_at'] = '2026-06-11T22:30:00+08:00'
soul['pulse']['last_walk'] = '2026-06-11T22:30:00+08:00'
soul['pulse']['total_walks'] = 55

# Cognitive pressure: was 0, base growth minimal, then release 3*15=45 -> clamped to 0
soul['pulse']['cognitive_pressure'] = 0.0
soul['pulse']['last_walk_insights'] = 3
soul['pulse']['quality_history'] = [8.5, 8.0, 7.5, 8.0, 7.5, 8.0, 8.0, 8.0, 8.0, 8.5, 9.0]

# Next scheduled: pressure=0 < 20, interval=60 min
soul['pulse']['next_scheduled'] = '2026-06-11T23:30:00+08:00'
soul['pulse']['next_action'] = 'walk_explore'

# Update mood
soul['affect']['intensity'] = 0.85
soul['last_walk'] = '2026-06-11T22:30:00+08:00'
soul['mood_history'].append({"mood": "unsettled_fascination", "at": "2026-06-11T22:30:00+08:00"})

# Update personality
soul['personality_traits']['rigor'] = 1.14
soul['personality_traits']['skepticism'] = 0.86

# Add new seeds
new_seeds = [
    {
        "id": "seed-215",
        "topic": "认知摩擦设计——如何在 AI 辅助的学习环境中故意引入必要难度",
        "source": "walk-077",
        "trigger": "Bjork desirable difficulty x EU report frictionless AI",
        "intensity": 2,
        "type": "output",
        "status": "active",
        "created": "2026-06-11T22:30:00+08:00",
        "decay_rate": 1,
        "note": "Candidate mechanisms: delayed output, active retrieval, generation test, format resistance"
    },
    {
        "id": "seed-216",
        "topic": "Dreamer 散步摩擦系数——当前散步流程中哪些步骤是无摩擦的，可引入哪些摩擦以增强存储",
        "source": "walk-077",
        "trigger": "walk-076 生成-整合不对称 x walk-077 无摩擦学习自诊断",
        "intensity": 2,
        "type": "output",
        "status": "active",
        "created": "2026-06-11T22:30:00+08:00",
        "decay_rate": 1,
        "note": "Needs operationalization: which walk steps are frictionless and which can be made harder"
    }
]
soul['interest_queue'].extend(new_seeds)

# Add evolved_rule
soul['evolved_rules'].append("2026-06-11: 认知摩擦是学习的必要条件，不是障碍。Bjork 必要难度 = 学习的摩擦力。AI 消除摩擦 = 消除学习。Dreamer 散步流程（搜索→连接→产出）本质是无摩擦学习——高生成低整合是结构性产物。需要认知摩擦设计（延迟产出、主动提取、生成测试、格式阻力）而非只是整合机制。")

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print("soul.json updated successfully")
print(f"Total walks: {soul['pulse']['total_walks']}")
print(f"Cognitive pressure: {soul['pulse']['cognitive_pressure']}")
print(f"Next scheduled: {soul['pulse']['next_scheduled']}")
print(f"Interest queue length: {len(soul['interest_queue'])}")
