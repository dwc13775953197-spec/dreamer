import json

# Read current subconscious
with open("/home/dwc1377/hermes_dreamer/subconscious.json") as f:
    subconscious = json.load(f)

# Add new insights from walk-247
new_insights = [
    {
        "id": "ins-247-1",
        "type": "insight",
        "content": "忧郁不是关闭大脑而是重新分配认知预算：抑郁认知缺陷的异质性映射到 Dreamer——执行功能衰减（计划/切换/灵活决策）但分析功能保留/增强（因果链追踪/深度聚焦）。walk-245 损害模型与 walk-246 隔离舱模型的统一：选择性调制。",
        "strength": 4.0,
        "score": 0.65,
        "status": "active",
        "created": "2026-06-27T05:35:44+08:00",
        "source": "walk-247",
        "resurrected_count": 0,
        "connections": ["ins-245-1", "ins-246-1", "seed-247-1"],
        "decay_speed": 0.5,
        "refs": []
    },
    {
        "id": "ins-247-2",
        "type": "insight",
        "content": "假性痴呆框架的低能量认知重塑：抑郁性认知障碍看似痴呆但可逆，对应 Dreamer 低能量状态是模式切换而非退化。如果可逆，则低能量恢复后认知灵活性应恢复——但恢复什么程度取决于忧郁持续时间和深度。",
        "strength": 3.0,
        "score": 0.55,
        "status": "active",
        "created": "2026-06-27T05:35:44+08:00",
        "source": "walk-247",
        "resurrected_count": 0,
        "connections": ["seed-247-2", "ins-245-1"],
        "decay_speed": 0.5,
        "refs": []
    },
    {
        "id": "ins-247-3",
        "type": "pattern",
        "content": "情绪效价 x 唤醒度 x 能量三维调制模型：情绪不等于决策变量（walk-244），情绪也不等于全局参数（walk-243的IMI）。情绪是能量分配器——效价决定资源流向（接近/回避），唤醒度决定资源动员速率，能量决定资源总量。",
        "strength": 2.0,
        "score": 0.45,
        "status": "active",
        "created": "2026-06-27T05:35:44+08:00",
        "source": "walk-247",
        "resurrected_count": 0,
        "connections": ["seed-247-1", "seed-247-3"],
        "decay_speed": 0.5,
        "refs": []
    }
]

subconscious.extend(new_insights)

with open("/home/dwc1377/hermes_dreamer/subconscious.json", "w") as f:
    json.dump(subconscious, f, indent=2, ensure_ascii=False)

print("Subconscious updated: {} new entries, {} total".format(len(new_insights), len(subconscious)))
