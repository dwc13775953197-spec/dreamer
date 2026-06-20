
import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    subconscious = json.load(f)

now = '2026-06-20T18:49:00+08:00'
new_entries = [
    {
        'id': 'walk162-insight1',
        'type': 'insight',
        'content': 'Dreamer 引用系统是 engram 竞争，不是检索。缺少抑制性平衡机制导致引用集中度升高。',
        'strength': 4.0,
        'connections': ['walk-159', 'walk-056', 'walk-059', 'walk-151'],
        'created': now,
        'last_accessed': now,
        'mature': 0.1,
        'status': 'active'
    },
    {
        'id': 'walk162-insight2',
        'type': 'insight',
        'content': 'DORMANT 衰减应从均匀改为引用频率调制的差异衰减：被引用越多衰减越慢。',
        'strength': 3.5,
        'connections': ['walk-151', 'walk-161', 'walk-009'],
        'created': now,
        'last_accessed': now,
        'mature': 0.1,
        'status': 'active'
    },
    {
        'id': 'walk162-insight3',
        'type': 'insight',
        'content': '空白区域可类比为 engram-to-be。DORMANT 为未来连接预设拓扑。双分布是临界系统标志。',
        'strength': 3.0,
        'connections': ['walk-010', 'walk-161'],
        'created': now,
        'last_accessed': now,
        'mature': 0.1,
        'status': 'active'
    }
]

subconscious.extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(subconscious, f, indent=2, ensure_ascii=False)

print(f'subconscious.json updated: {len(subconscious)} entries total')
