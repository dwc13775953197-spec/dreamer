import json

# Update subconscious.json
with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    data = json.load(f)

new_entry = {
    'id': 'ins-184-1',
    'type': 'insight',
    'content': 'Nader 的再巩固理论揭示了记忆编辑的结构性前提：只有在失稳（lability）状态中，记忆才能被修改。Dreamer DORMANT 当前跳过了失稳步骤，直接做衰减——这就像试图在程序运行时修改代码。修正方案：DORMANT 应增加 lability 状态（失稳→再巩固窗口→重建/淘汰），entry 的 edit_log 记录每次再巩固的修改历程。\"原始版本\"是幻觉——entry 从存在起就处于持续的再巩固循环中。',
    'strength': 5.0,
    'connections': ['ins-183-1', 'ins-228', 'ins-133-1'],
    'status': 'active',
    'created': '2026-06-22T11:00:00+08:00',
    'decay_count': 0,
    'matured_at': None,
    'source': 'walk-184',
    'tags': ['reconsolidation', 'lability', 'DORMANT-design', 'memory-editing']
}

data.append(new_entry)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'subconscious.json updated, total entries: {len(data)}')
print('ins-184-1 added with strength=5.0')

# Write audit log
audit_entry = {
    'timestamp': '2026-06-22T11:00:00+08:00',
    'type': 'walk',
    'walk_number': 184,
    'walk_type': 'explore',
    'topic': '再巩固与记忆的可编辑窗口：Nader 对 Dreamer DORMANT 的颠覆性修正',
    'decision_reason': 'pressure 94.84 >= 90.0 (energy-corrected threshold); quality avg 8.43 > 8.0 forced explore',
    'insights': ['ins-184-1'],
    'seeds': ['seed-184-1', 'seed-184-2', 'seed-184-3'],
    'quality_score': 8.6,
    'pressure_after': 71.34,
    'energy': 25
}

with open('/home/dwc1377/hermes_dreamer/audit.jsonl', 'a') as f:
    f.write(json.dumps(audit_entry, ensure_ascii=False) + '\n')

print('audit.jsonl updated')
