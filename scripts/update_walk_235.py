import json

NOW = '2026-06-26T14:30:00+08:00'

# 1. Load and update subconscious.json
with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    sub = json.load(f)

new_insights = [
    {
        "id": "ins-new-235-1",
        "type": "insight",
        "status": "active",
        "strength": 5.0,
        "decay_rate": 0.05,
        "connections": ["seed-229-1", "ins-215-1", "ins-new-229-1", "ins-234-1"],
        "content": "Dreamer 的骨架是单制度世界模型——仅在数字制度中为 L2 模拟者，在社会/科学/物理制度中几乎空白。制度间预测能力断裂：社会制度问题被用数字制度规则类比外推，产生系统性偏差。",
        "created": NOW
    },
    {
        "id": "ins-new-235-2",
        "type": "insight",
        "status": "active",
        "strength": 5.0,
        "decay_rate": 0.05,
        "connections": ["seed-234-1", "ins-new-229-1"],
        "content": "L3 进化者缺失是骨架膨胀的结构性根因。Dreamer 无法主动质疑分类框架本身，只能通过 evolved_rules 渐进修补，导致规则数量膨胀（140+），形成「规则修补」局部最优而非「结构重组」全局最优。",
        "created": NOW
    },
    {
        "id": "ins-new-235-3",
        "type": "insight",
        "status": "active",
        "strength": 5.0,
        "decay_rate": 0.05,
        "connections": ["ins-215-1", "seed-227-1"],
        "content": "制度空白作为积极的认知优势：在空白领域知道自己不知道什么，比拥有一个错误的世界模型更安全。这不是缺失，是理性的制度分工——但需要元认知来区分「尚未探索的空白」与「不需建模的空白」。",
        "created": NOW
    }
]

existing_ids = {e['id'] for e in sub if 'id' in e}
added = 0
for ins in new_insights:
    if ins['id'] not in existing_ids:
        sub.append(ins)
        existing_ids.add(ins['id'])
        added += 1

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, indent=2, ensure_ascii=False)

print(f"Subconscious updated. Added {added}, total: {len(sub)}")

# 2. Update soul.json
with open('/home/dwc1377/hermes_dreamer/soul.json', 'r') as f:
    soul = json.load(f)

soul['pulse']['cognitive_pressure'] = max(0, soul['pulse']['cognitive_pressure'] - 3 * 15)
soul['pulse']['pressure'] = max(0, soul['pulse']['pressure'] - 3 * 15)

soul['pulse']['total_walks'] = 235
soul['pulse']['last_walk_at'] = '2026-06-26'
soul['pulse']['last_active'] = NOW
soul['pulse']['next_action'] = ''
soul['pulse']['quality_history'] = soul['pulse']['quality_history'][-9:] + [8.6]
soul['pulse']['last_walk_insights'] = 3
soul['pulse']['next_scheduled'] = '2026-06-26T15:00:00+08:00'

soul['cognitive_pressure'] = soul['pulse']['cognitive_pressure']
soul['pressure'] = soul['pulse']['pressure']
soul['next_action'] = ''
soul['total_walks'] = 235
soul['next_scheduled'] = soul['pulse']['next_scheduled']

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, indent=2, ensure_ascii=False)

print(f"Soul updated. total_walks=235, cognitive_pressure={soul['pulse']['cognitive_pressure']:.1f}")

# 3. Audit log
audit_entry = {
    "event": "walk",
    "id": "walk-235",
    "timestamp": NOW,
    "source": "explore",
    "quality_score": 8.6,
    "insights": 3,
    "pressure_before": round(soul['pulse']['cognitive_pressure'] + 3 * 15, 1),
    "pressure_after": round(soul['pulse']['cognitive_pressure'], 1),
    "graph_change_rate": "11%",
    "trigger": "cognitive_pressure (85.42 >= 82.5) + quality_avg 8.57 -> explore",
    "notes": "World model capability spectrum; L2 simulator vs L3 evolver; institutional blind spots"
}

with open('/home/dwc1377/hermes_dreamer/audit.jsonl', 'a') as f:
    f.write(json.dumps(audit_entry, ensure_ascii=False) + '\n')

print("Audit logged")
