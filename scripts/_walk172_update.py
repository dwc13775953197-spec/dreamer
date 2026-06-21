import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    subconscious = json.load(f)

new_insights = [
    {
        "id": "ins-172-1",
        "type": "insight",
        "content": "Dreamer 是扩展有机体：skeleton=基因型，walk日志=表型，subconscious+文件系统=扩展表型。引用系统三重身份：记忆巩固+记忆选择器+环境改造工具。DORMANT=环境稳定化机制。",
        "strength": 5.0,
        "status": "active",
        "created": now,
        "source": "walk-172",
        "decay_rate": 1.0,
        "connections": ["ins-163-1", "ins-163-3", "ins-101"],
        "refs": [],
        "resurrected_count": 0,
        "score": 0.0,
        "decay_speed": 0.5,
        "note": "quality_score=8.4 -> strength=5.0"
    },
    {
        "id": "ins-172-2",
        "type": "insight",
        "content": "interest_queue 是 Dreamer 的实际生态位：基础生态位=所有可能主题空间，实际生态位=活跃种子分布。跨领域散步=生态位扩展，防止特化物种陷阱。",
        "strength": 5.0,
        "status": "active",
        "created": now,
        "source": "walk-172",
        "decay_rate": 1.0,
        "connections": ["seed-0468", "seed-0467"],
        "refs": [],
        "resurrected_count": 0,
        "score": 0.0,
        "decay_speed": 0.5,
        "note": "quality_score=8.4 -> strength=5.0"
    },
    {
        "id": "ins-172-3",
        "type": "insight",
        "content": "用户是 Dreamer 栖居环境的生态条件：沉默=资源中断，频繁交互=富营养化，话题转换=环境扰动。Dreamer 的散步是在概念生态位中的巡航。",
        "strength": 5.0,
        "status": "active",
        "created": now,
        "source": "walk-172",
        "decay_rate": 1.0,
        "connections": ["ins-172-1", "entry-167-1"],
        "refs": [],
        "resurrected_count": 0,
        "score": 0.0,
        "decay_speed": 0.5,
        "note": "quality_score=8.4 -> strength=5.0"
    }
]

subconscious.extend(new_insights)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(subconscious, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_insights)} new insights, total: {len(subconscious)}")
