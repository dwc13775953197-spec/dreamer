import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

if isinstance(sub, list):
    entries = sub
    sub = {'entries': entries, 'version': 1}
elif isinstance(sub, dict) and 'entries' not in sub:
    sub['entries'] = []

new_insights = [
    {
        'type': 'insight',
        'content': 'Dreamer 缺少 Walk Initializer——标准化的入职流程让每次散步在 30 秒内建立状态理解，而不是从 soul.json 的原始 JSON 中自行推断。Anthropic Harness 的 Initializer Agent 是模板。',
        'strength': 3.0,
        'score': 0.3,
        'source': 'walk-114',
        'created': '2026-06-16T21:30:00+08:00',
        'decay_rate': 1
    },
    {
        'type': 'insight',
        'content': '格式约束即认知约束——frontmatter 的结构化字段不是形式主义，是限制 agent 认知行为的脚手架。JSON vs Markdown 的选择背后是结构化 vs 自由编辑的行为约束差异。',
        'strength': 3.0,
        'score': 0.3,
        'source': 'walk-114',
        'created': '2026-06-16T21:30:00+08:00',
        'decay_rate': 1
    },
    {
        'type': 'insight',
        'content': '可合并状态应作为散步结束的不变量——骨架整洁（无半成品连接点）、潜意识无重复（Merge 写入时执行）、interest_queue 更新、日志可读。',
        'strength': 3.0,
        'score': 0.3,
        'source': 'walk-114',
        'created': '2026-06-16T21:30:00+08:00',
        'decay_rate': 1
    }
]

for ni in new_insights:
    sub['entries'].append(ni)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, ensure_ascii=False, indent=2)

print(f'Added 3 insights. Total entries: {len(sub["entries"])}')
