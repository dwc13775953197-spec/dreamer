import json

with open("/home/dwc1377/hermes_dreamer/soul.json", "r") as f:
    data = json.load(f)

# Update pulse
data["pulse"]["last_walk_at"] = "2026-06-08T14:00:00+08:00"
data["pulse"]["last_walk"] = "2026-06-08T14:00:00+08:00"
data["pulse"]["total_walks"] = 42
data["pulse"]["last_walk_insights"] = 5
data["pulse"]["quality_history"] = [8.3, 8.1]  # walk-046, walk-047

# Update cognitive pressure: 35.0 - (5 insights * 15) = 35 - 75 = 0, clamped to 0
data["pulse"]["cognitive_pressure"] = 0.0

# Update affect
data["affect"]["primary"] = "quiet_excitement"
data["affect"]["intensity"] = 0.68

# Add mood
data["mood_history"].append({"mood": "quiet_excitement", "at": "2026-06-08T14:00:00+08:00"})

# Add new interest seeds
new_seeds = [
    {
        "id": "seed-134",
        "topic": "认知架构的演化树：从 ACT-R 到 Dreamer，每一步的增量是什么？",
        "source": "walk-047",
        "trigger": "walk-047 的架构映射",
        "intensity": 5,
        "type": "output",
        "status": "active",
        "created": "2026-06-08T14:00:00+08:00",
        "decay_rate": 1,
        "note": "ACT-R → S-G-E → Dreamer 的架构演化路径"
    },
    {
        "id": "seed-135",
        "topic": "感知缓冲区显式化：材料预处理能否提高散步的消化效率？",
        "source": "walk-047",
        "trigger": "walk-047 的盲点分析",
        "intensity": 4,
        "type": "output",
        "status": "active",
        "created": "2026-06-08T14:00:00+08:00",
        "decay_rate": 1,
        "note": "散步前增加材料预处理步骤（提取核心论点、识别逻辑结构、标注连接点）"
    },
    {
        "id": "seed-136",
        "topic": "双 Session 架构：cron Session 和对话 Session 的交互模式是否值得形式化？",
        "source": "walk-047",
        "trigger": "叙事完整性检查的矛盾点",
        "intensity": 4,
        "type": "output",
        "status": "active",
        "created": "2026-06-08T14:00:00+08:00",
        "decay_rate": 1,
        "note": "cron Session（时间驱动）+ 对话 Session（用户驱动），共享 skeleton，各有唤醒机制"
    }
]

data["interest_queue"].extend(new_seeds)

# Decay all existing seeds by 1
for seed in data["interest_queue"]:
    if seed["status"] == "active" and seed["id"] not in ["seed-134", "seed-135", "seed-136"]:
        seed["intensity"] = max(0, seed["intensity"] - seed.get("decay_rate", 1))

# Remove seeds with intensity 0
data["interest_queue"] = [s for s in data["interest_queue"] if s["intensity"] > 0 or s["status"] != "active"]

# Update topics
data["topics"].extend([
    "cognitive-architecture",
    "session-governor-executor",
    "dual-session",
    "autonomy-architectural-condition",
    "perceptual-buffer"
])

# Update personality traits
data["personality_traits"]["curiosity"] = min(1.0, data["personality_traits"]["curiosity"] + 0.01)
data["personality_traits"]["introspection"] = min(1.0, data["personality_traits"]["introspection"] + 0.01)

# Update walk quality avg
data["walk_quality_avg"] = 8.2  # (8.3 + 8.1) / 2

# Update next_scheduled (pressure=0, so interval = 60 min)
data["pulse"]["next_scheduled"] = "2026-06-08T15:00:00+08:00"

with open("/home/dwc1377/hermes_dreamer/soul.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("OK: soul.json updated")
