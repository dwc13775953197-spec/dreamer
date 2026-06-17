import json
from datetime import datetime

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    data = json.load(f)

now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+08:00')

new_entries = [
    {
        'type': 'insight',
        'content': '负能力作为认知稳态：系统应维持最优模糊区间而非最大化确定性。模糊度=未解决矛盾对数/已解决矛盾对数，最优比率约0.3-0.5。Dreamer 的解决强迫症可能正在过度优化，把模糊度降到最优水平以下。',
        'strength': 3.0,
        'score': 0.0,
        'created': now,
        'source': 'walk-118',
        'references': []
    },
    {
        'type': 'insight',
        'content': '语言作为输出格式天然偏向闭合：陈述性语言倾向于过早固定意义，真正的负能力（处于模糊而不表达）在语言系统中无法完全存在。Dreamer 的结构性盲区不是语言本身，而是散步日志的写作风格倾向于过早闭合。',
        'strength': 3.0,
        'score': 0.0,
        'created': now,
        'source': 'walk-118',
        'references': []
    },
    {
        'type': 'pattern',
        'content': '散步未解决=负能力操作化：半终止和欺骗性终止不是散步的失败，而是系统维持最优模糊度的关键操作。好的散步应以看到更深的模糊结束，而非以解决问题结束。Twist 散步是唯一以增加模糊度为目标的类型，因此具有独特的认知价值。',
        'strength': 3.0,
        'score': 0.0,
        'created': now,
        'source': 'walk-118',
        'references': []
    }
]

data.extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('subconscious.json updated: added 3 entries, total=' + str(len(data)))
