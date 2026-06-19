import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    data = json.load(f)

new_entries = [
    {
        "id": "insight-143-1",
        "type": "insight",
        "content": "连接是记忆的突触，不只是装饰。connections 字段具有双重功能：导航（索引路径）+ 巩固（图拓扑衰减抗性）。缺少 connections = 没有突触的神经元：存在但无法被激活。",
        "strength": 5.0,
        "score": 0.0,
        "connections": ["ins-135-1", "ins-133-3", "entry-061"],
        "created": "2026-06-19T16:25:00+08:00",
        "source": "walk-143",
        "status": "active",
        "resurrected_count": 0,
        "decay_speed": 0.5,
        "refs": [],
        "note": "quality_score 8.5, initial strength 5.0"
    },
    {
        "id": "insight-143-2",
        "type": "insight",
        "content": "巩固的悖论：连接越多越难连接。系统巩固需要空闲认知带宽——如果 subconscious 持续被新信息填满，就没有资源指导皮层重组。30% 零产出散步的理论基础：巩固需要空余认知带宽。",
        "strength": 5.0,
        "score": 0.0,
        "connections": ["insight-143-1", "ins-131-1", "ins-133-1"],
        "created": "2026-06-19T16:25:00+08:00",
        "source": "walk-143",
        "status": "active",
        "resurrected_count": 0,
        "decay_speed": 0.5,
        "refs": [],
        "note": "quality_score 8.5, initial strength 5.0"
    },
    {
        "id": "insight-143-3",
        "type": "insight",
        "content": "系统巩固发生在散步中（合成代谢），不在 DORMANT 中（分解代谢）。散步流程应增加连接建立作为独立步骤，确保每次至少 20% 时间建立已有 entry 之间的连接。",
        "strength": 5.0,
        "score": 0.0,
        "connections": ["insight-143-2", "ins-133-1", "ins-133-2"],
        "created": "2026-06-19T16:25:00+08:00",
        "source": "walk-143",
        "status": "active",
        "resurrected_count": 0,
        "decay_speed": 0.5,
        "refs": [],
        "note": "quality_score 8.5, initial strength 5.0"
    }
]

data.extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added 3 new entries. Total: {len(data)}")
