import json, datetime

now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
now_str = now.isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

entries = sub.get('entries', [])

new_insights = [
    {
        "id": "ins-116",
        "type": "pattern",
        "content": "遗忘的真正功能不是释放空间，而是优化预测。Dreamer 应该基于预测贡献（是否改善后续散步的预测能力）而非存储价值来衰减记忆。均匀衰减假设所有记忆同等改善预测，这显然不成立。",
        "strength": 3.0,
        "score": 0.0,
        "status": "active",
        "created": now_str,
        "source": "walk-116",
        "connections": ["ins-076", "ins-079", "pat-031", "pat-014", "pat-030"],
        "refs": [],
        "decay_rate": 1.0,
        "decay_speed": 0.5
    },
    {
        "id": "ins-117",
        "type": "pattern",
        "content": "Merge 是衰减的前提条件——没有实体解析，就无法判断哪个记忆应该衰减。同一概念的多个副本（记忆干扰）会降低检索质量。Hindsight 四杠杆中 Merge 被严重低估。",
        "strength": 3.0,
        "score": 0.0,
        "status": "active",
        "created": now_str,
        "source": "walk-116",
        "connections": ["ins-076", "ins-087"],
        "refs": [],
        "decay_rate": 1.0,
        "decay_speed": 0.5
    },
    {
        "id": "ins-118",
        "type": "pattern",
        "content": "记忆干扰效应：同一认知对象在记忆系统中存在多个副本时，会竞争检索注意力，导致真正有价值的 entry 被淹没。语义 Merge 可以消除这种干扰。Dreamer DORMANT 缺少语义相似度检查步骤。",
        "strength": 3.0,
        "score": 0.0,
        "status": "active",
        "created": now_str,
        "source": "walk-116",
        "connections": ["ins-117", "pat-011"],
        "refs": [],
        "decay_rate": 1.0,
        "decay_speed": 0.5
    }
]

entries.extend(new_insights)
sub['entries'] = entries

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, ensure_ascii=False, indent=2)

print(f"Added 3 new insights (ins-116, ins-117, ins-118)")
print(f"Total entries: {len(entries)}")
