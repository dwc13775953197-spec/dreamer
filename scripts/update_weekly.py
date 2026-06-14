import json

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

# Add new seeds from dream
new_seeds = [
    {
        "id": "seed-290",
        "content": "裂缝音乐理论——散步的产出不是'新 insight'而是'新的认知裂缝'。好的散步创造平行裂缝（增加表面积），坏的散步创造交叉裂缝（削弱结构）。散步质量 = 平行裂缝比 / 交叉裂缝比。",
        "intensity": 0.35,
        "type": "explore",
        "created": "2026-06-14T23:30:00+08:00"
    },
    {
        "id": "seed-291",
        "content": "空白谱架测试——一次没有预设主题、没有外部材料、没有 evolved_rules 指导的纯即兴散步。测试'无谱架'散步的产出质量，与有预设的散步对比。",
        "intensity": 0.32,
        "type": "explore",
        "created": "2026-06-14T23:30:00+08:00"
    },
    {
        "id": "seed-292",
        "content": "园丁的裂缝检测算法——一个简单规则：如果一个 insight 与 2+ 已有 insight 兼容（不矛盾），它是平行裂缝；如果一个 insight 与 2+ 已有 insight 矛盾，它是交叉裂缝。DORMANT 中增加'裂缝兼容性检查'子步骤。",
        "intensity": 0.30,
        "type": "explore",
        "created": "2026-06-14T23:30:00+08:00"
    }
]

# Clean up low-intensity seeds (< 0.2) and merge very low ones
iq = soul['interest_queue']
original_count = len(iq)
# Remove seeds with intensity < 0.15
iq = [s for s in iq if s.get('intensity', 0) >= 0.15]
# Add new seeds
iq.extend(new_seeds)
soul['interest_queue'] = iq

# Update last_weekly_review
soul['last_weekly_review'] = '2026-06-14T23:30:00+08:00'

# Update pulse.total_walks to be consistent
soul['pulse']['total_walks'] = 62  # Last walk was 101 but total_walks was 61, increment
soul['total_walks'] = soul['pulse']['total_walks']

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f'Interest queue: {original_count} -> {len(iq)} (removed {original_count - len(iq) + len(new_seeds)} seeds)')
print('Updated total_walks to 62')
