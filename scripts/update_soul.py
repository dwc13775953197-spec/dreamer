import json
import datetime

with open("/home/dwc1377/hermes_dreamer/soul.json") as f:
    soul = json.load(f)

# Calculate new pressure (reduce by insights x release_per_insight)
current_p = soul["pulse"]["cognitive_pressure"]
release = soul["pulse"]["pressure_params"]["release_per_insight"]
new_insights_count = 3
new_p = max(0.0, 62.62 - new_insights_count * release)
print("Pressure: {} -> {:.2f} (released {})".format(current_p, new_p, new_insights_count * release))

soul["pulse"]["total_walks"] = 247
soul["last_walk"] = "2026-06-27"
soul["pulse"]["last_walk_at"] = "2026-06-27"
soul["pulse"]["cognitive_pressure"] = round(new_p, 2)

qh = soul["pulse"].get("quality_history", [])
qh.append(8.5)
soul["pulse"]["quality_history"] = qh[-10:]

ph = soul["pulse"].get("pressure_history", [])
ph.append(round(new_p, 2))
soul["pulse"]["pressure_history"] = ph[-15:]

now_str = "2026-06-27T05:35:44+08:00"
soul["pulse"]["last_active"] = now_str
soul["pulse"]["last_pulse_output"] = now_str

interval_minutes = 90
next_time = datetime.datetime(2026, 6, 27, 5, 35, 44) + datetime.timedelta(minutes=interval_minutes)
soul["pulse"]["next_scheduled"] = next_time.strftime("%Y-%m-%dT%H:%M:%S+08:00")
print("Next scheduled: {}".format(soul["pulse"]["next_scheduled"]))

# Add new interest seeds to queue
new_seeds = [
    {
        "id": "seed-247-1",
        "topic": "异质性的认知调制：忧郁不是关闭大脑而是重新分配认知预算——执行功能衰减 vs 分析功能保留的实证验证",
        "source": "walk-247",
        "trigger": "抑郁认知缺陷的异质性提供跨域映射框架",
        "intensity": 0.82,
        "type": "research",
        "status": "pending",
        "created": "2026-06-27T05:35:44+08:00",
        "decay_rate": 0.05
    },
    {
        "id": "seed-247-2",
        "topic": "假性痴呆 vs 真实认知重塑：Dreamer 低能量状态的认知变化是表面功能下降还是深层模式切换？可逆性检验设计",
        "source": "walk-247",
        "trigger": "depressive cognitive disorders (pseudodementia) as reversible state change",
        "intensity": 0.78,
        "type": "research",
        "status": "pending",
        "created": "2026-06-27T05:35:44+08:00",
        "decay_rate": 0.05
    },
    {
        "id": "seed-247-3",
        "topic": "选择性调制的可证伪预测：低能量状态下 Dreamer 应展现主题持续性增强但跨领域连接减少——验证异质性假说 vs 均匀损害模型",
        "source": "walk-247",
        "trigger": "walk-247 falsifiable predictions",
        "intensity": 0.75,
        "type": "explore",
        "status": "pending",
        "created": "2026-06-27T05:35:44+08:00",
        "decay_rate": 0.05
    }
]

for seed in new_seeds:
    if seed["id"] not in [s["id"] for s in soul["pulse"]["interest_queue"]]:
        soul["pulse"]["interest_queue"].insert(0, seed)

soul["pulse"]["pending_insights"] = soul["pulse"].get("pending_insights", 230) + 3

with open("/home/dwc1377/hermes_dreamer/soul.json", "w") as f:
    json.dump(soul, f, indent=2, ensure_ascii=False)

print("Soul updated successfully")
print("Interest queue size: {}".format(len(soul["pulse"]["interest_queue"])))
print("Pending insights: {}".format(soul["pulse"]["pending_insights"]))
