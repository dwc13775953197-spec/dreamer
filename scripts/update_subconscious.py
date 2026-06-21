
import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    data = json.load(f)

new_insight = {
    "id": "ins-183-1",
    "type": "insight",
    "content": "Albouy 2026 的睡眠重激活研究为 Dreamer DORMANT 提供了生物学锚点：巩固不是被动存储而是主动编辑。DORMANT 应增加选择性重激活步骤——选中等强度+高连接度的 entry，用当前 skeleton 碰撞再编码，连续失败转候选淘汰。这比均匀衰减更接近生物现实。",
    "strength": 3.0,
    "status": "active",
    "created": "2026-06-22T10:30:00+08:00",
    "source": "walk-183",
    "decay_rate": 0.03,
    "decayed_at": None,
    "resurrected_count": 0,
    "score": 0.0,
    "connections": ["ins-133-1", "ins-135-1", "ins-228"],
    "refs": ["Albouy 2026", "Bjork necessary difficulty", "Hindsight 4-lever"],
    "decay_speed": 1.0,
    "note": "quality_score 8.4, strength 3.0"
}

data.append(new_insight)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"subconscious.json updated. Total entries: {len(data)}")
