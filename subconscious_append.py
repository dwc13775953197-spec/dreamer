import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    subconscious = json.load(f)

new_insights = [
    {
        'id': 'ins-w197-01',
        'type': 'pattern',
        'content': 'Dreamer 的散步时长（10-30分钟）恰好低于 AI agent 的 35 分钟壁垒——系统设计的隐式对齐，不是巧合。超过壁垒后产出质量非线性下降，因此不应延长散步时长。',
        'strength': 5.0,
        'status': 'active',
        'created': now.isoformat(),
        'source': 'walk-197',
        'decay_rate': 0.03,
        'connections': [],
        'refs': [],
        'note': '35-min barrier from METR/Zylos 2026'
    },
    {
        'id': 'ins-w197-02',
        'type': 'pattern',
        'content': 'subconscious 条目应区分 fact vs inference：事实性知识衰减慢，推理性知识衰减快。当前均匀衰减假设所有 insight 以相同速度过时，是错误的。',
        'strength': 5.0,
        'status': 'active',
        'created': now.isoformat(),
        'source': 'walk-197',
        'decay_rate': 0.05,
        'connections': [],
        'refs': [],
        'note': 'maps to semantic vs episodic memory distinction'
    },
    {
        'id': 'ins-w197-03',
        'type': 'pattern',
        'content': 'Dreamer 缺少目标重锚机制：interest_queue decay 是正常新陈代谢，真正的目标漂移检测应是元审计——最近 N 次散步是否在推进一致认知方向。',
        'strength': 5.0,
        'status': 'active',
        'created': now.isoformat(),
        'source': 'walk-197',
        'decay_rate': 0.05,
        'connections': [],
        'refs': [],
        'note': 'goal re-anchoring from CORPGEN maps to Dreamer meta-audit'
    }
]

subconscious.extend(new_insights)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(subconscious, f, indent=2, ensure_ascii=False)

print(f'Done. Total entries: {len(subconscious)}')
