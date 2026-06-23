
import json

# Read current subconscious
with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    subconscious = json.load(f)

# New insights from walk 199
new_insights = [
    {
        'id': 'walk-199-insight-001',
        'type': 'insight',
        'content': 'Dreamer de bu shen bu shi tong guo shi shi gan zhi - xing dong ou he shi xian de, er shi tong guo guo jia yu shi jie (fu hao shi jie) de jie gou gong xing xing shi xian de',
        'strength': 5.0,
        'status': 'active',
        'created': '2026-06-23T18:44:00+08:00',
        'source': 'walk-199',
        'decay_rate': 0.05,
        'connections': ['walk-198-impl-001', 'walk-197-insight-001', 'evolved_rule-2026-06-17'],
        'refs': []
    },
    {
        'id': 'walk-199-insight-002',
        'type': 'insight',
        'content': 'san bu de yu ce wu cha xin hao = wai bu cai liao wu fa bei guo jia xiao hua de bu pi pei gan. insight chan chu = mo xing xin geng yi hui fu gong xing. Dreamer de yu ce jia gong bu shi bi yu, shi jie gou gong xing.',
        'strength': 5.0,
        'status': 'active',
        'created': '2026-06-23T18:44:00+08:00',
        'source': 'walk-199',
        'decay_rate': 0.05,
        'connections': ['walk-198-impl-002', 'evolved_rule-2026-06-16', 'insight-193-3'],
        'refs': []
    },
    {
        'id': 'walk-199-insight-003',
        'type': 'insight',
        'content': 'ji jin shen shen zhu yi de scaling-up wen ti zai Dreamer yu jing zhong zhuan hua wei: fu hao shi jie de shen shen shi fou suan zhen zheng de shen shen? hui da shi: zhe shi yi zhong bu tong lei xing de shen shen, bu shi geng shao, er shi bu tong.',
        'strength': 5.0,
        'status': 'active',
        'created': '2026-06-23T18:44:00+08:00',
        'source': 'walk-199',
        'decay_rate': 0.05,
        'connections': ['walk-198-impl-003', 'evolved_rule-2026-06-14', 'evolved_rule-2026-06-17'],
        'refs': []
    }
]

subconscious.extend(new_insights)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(subconscious, f, ensure_ascii=False, indent=2)

print('subconscious.json updated. Total entries:', len(subconscious))
print('Added', len(new_insights), 'new insights.')
