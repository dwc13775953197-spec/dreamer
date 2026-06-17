import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)

audit = {
    "timestamp": now.isoformat(),
    "action": "walk",
    "walk_number": 123,
    "walk_type": "explore",
    "trigger": "pressure 45.67 >= effective_threshold 42.0 (curiosity 1.17 > 0.9), quality_trend 8.33 > 8.0 forced explore",
    "topic": "AI创作的可控失控：Dreamer散步作为创作控制系统",
    "stress_type": "Stretch",
    "quality_score": 7.5,
    "insights_added": 3,
    "pressure_after": 0.67,
    "seeds_added": 3,
    "seeds_total": 15,
    "corrections_found": 0,
    "conflicts_found": 0
}

with open("/home/dwc1377/hermes_dreamer/audit.jsonl", "a") as f:
    f.write(json.dumps(audit, ensure_ascii=False) + "\n")

print("Audit logged")
