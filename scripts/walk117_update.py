import json, datetime

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat()

new_entries = [
    {
        "id": "ins-082",
        "type": "insight",
        "content": "矛盾是认知增长的引擎，不是需要消除的 bug。认知失调理论的现代更新：适度的认知失调触发更深的认知加工，=Bjork 必要难度的心理学基础。Dreamer 的 DORMANT 倾向于消解矛盾（衰减/合并），但最有价值的矛盾应该被保留并标注。",
        "strength": 5.0,
        "created": now,
        "source": "walk-117",
        "cited_by": [],
        "tags": ["cognitive-dissonance", "contradiction", "learning-mechanism", "DORMANT-design"]
    },
    {
        "id": "ins-083",
        "type": "insight",
        "content": "矛盾有三种解决策略：消解（找到更高阶框架容纳两者）、保留（标注情境条件）、超越（范式转换——发现矛盾的前提假设本身是错误的）。超越是最有价值但最难实现的。walk-072 的功能转向（从建造骨架到使用骨架）本质上是一次范式转换。",
        "strength": 5.0,
        "created": now,
        "source": "walk-117",
        "cited_by": [],
        "tags": ["contradiction-resolution", "paradigm-shift", "functional-turn", "skeleton-cracks"]
    },
    {
        "id": "ins-084",
        "type": "insight",
        "content": "认知失调密度可以作为散步质量的新维度。一个从不遇到矛盾的散步可能是确认偏误散步。quality_score 应该包含：产出是否挑战了已有假设？是否修改了已有立场？新维度 = 矛盾数量 * 被综合（而非忽略）的比例。",
        "strength": 5.0,
        "created": now,
        "source": "walk-117",
        "cited_by": [],
        "tags": ["walk-quality", "cognitive-dissonance", "self-evaluation", "confirmation-bias"]
    }
]

sub["entries"].extend(new_entries)

with open("/home/dwc1377/hermes_dreamer/subconscious.json", "w") as f:
    json.dump(sub, f, ensure_ascii=False, indent=2)

print(f"Added 3 insights (ins-082, ins-083, ins-084) with strength 5.0")
print(f"Total entries: {len(sub['entries'])}")
