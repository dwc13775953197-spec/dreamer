import json
with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

soul['evolved_rules'].append('2026-06-17: 矛盾是认知增长的引擎，不是系统故障。DORMANT 应从"解决矛盾"转向"管理矛盾"——区分不完整性矛盾（需要更多信息）和内在矛盾性矛盾（即使无限信息也无法消解，反映现实本身的张力）。三种解决策略：消解（更高阶框架）/保留（标注情境条件）/超越（范式转换）。散步质量新维度：认知失调密度=矛盾数量×被综合比例。walk-117 验证了跨散步连接（反脆弱+预测加工→矛盾引擎）的高产出模式。')

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f'Added evolved rule. Total rules: {len(soul["evolved_rules"])}')
