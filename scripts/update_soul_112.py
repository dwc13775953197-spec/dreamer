import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

pulse = soul['pulse']
pulse['last_walk_at'] = now
pulse['last_walk'] = now
pulse['total_walks'] = pulse.get('total_walks', 69) + 1
pulse['last_active'] = now

pressure = pulse['cognitive_pressure']
pressure -= (4 * pulse['pressure_params']['release_per_insight'])
pressure = max(0, min(100, pressure))
pulse['cognitive_pressure'] = round(pressure, 2)

pulse['quality_history'].append(8.5)
pulse['quality_history'] = pulse['quality_history'][-10:]
pulse['last_walk_insights'] = 4
pulse['walk_quality_avg'] = round(sum(pulse['quality_history']) / len(pulse['quality_history']), 2)

pulse['pressure_history'].append(round(pressure, 2))
pulse['pressure_history'] = pulse['pressure_history'][-20:]

pulse['next_scheduled'] = (datetime.now(tz) + timedelta(minutes=60)).isoformat()

new_seeds = [
    {
        'id': 'seed-321',
        'topic': '记忆巩固四杠杆作为 DORMANT 2.0 设计框架：Importance/Merge/Decay/Eviction 如何映射到 Dreamer 架构？',
        'source': 'walk-112',
        'trigger': 'Hindsight Agent Memory Consolidation 四杠杆框架分析',
        'intensity': 0.65,
        'type': 'research',
        'status': 'pending',
        'created': now,
        'decay_rate': 1
    },
    {
        'id': 'seed-322',
        'topic': '认知对象索引：如何让骨架识别同一认知对象的不同表述？',
        'source': 'walk-112',
        'trigger': 'Hindsight Merge 杠杆 + 骨架冗余观察',
        'intensity': 0.55,
        'type': 'research',
        'status': 'pending',
        'created': now,
        'decay_rate': 1
    },
    {
        'id': 'seed-323',
        'topic': '双维度衰减 vs 均匀衰减：Dreamer DORMANT 是否需要情境性衰减？',
        'source': 'walk-112',
        'trigger': 'Hindsight Decay 杠杆 + walk-089 图拓扑衰减',
        'intensity': 0.6,
        'type': 'research',
        'status': 'pending',
        'created': now,
        'decay_rate': 1
    }
]

soul['interest_queue'].extend(new_seeds)

soul['mood'] = 'wonder'
soul['mood_history'].append({'mood': 'wonder', 'at': now})

soul['evolved_rules'].append(
    '2026-06-16: 记忆巩固四杠杆（Hindsight 2026）作为 DORMANT 2.0 设计框架。Importance=散步的结构化输出（什么改变了骨架），Merge=DORMANT 的实体解析子步骤（同一认知对象不同表述的合并），Decay=双维度衰减（结构性+情境性），Eviction=骨架的主动淘汰审查。当前 DORMANT 只覆盖 Decay 的一个子集（均匀衰减），其余三根杠杆完全缺失。这不是 bug，是设计空间。'
)

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print('soul.json updated: pressure={}, total_walks={}'.format(pressure, pulse['total_walks']))
