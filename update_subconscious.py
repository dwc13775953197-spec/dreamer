import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)
now_iso = now.isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    data = json.load(f)

new_insights = [
    {
        "id": "insight-141-1",
        "title": "Outsourcing theorem: single-thread metacognition is structurally incomplete",
        "type": "structural",
        "strength": 5.0,
        "created": now_iso,
        "source": "walk-141",
        "connections": ["evolved-rule-20260615-00", "walk-125-meta-cognition", "pat-014-capability-limits"],
        "summary": "Single-thread cognitive systems cannot self-monitor process during execution. This is a mathematical constraint, not a bug. Solution: out-of-band monitoring (user as external meta-cognitive resource) + finite recursion (two layers sufficient). Operationalization: embed meta_marks in walk logs as cheap signals for offline monitoring.",
        "status": "active",
        "matures_at": None
    },
    {
        "id": "insight-141-2",
        "title": "Effective honesty: graded labeling over binary certainty marking",
        "type": "process",
        "strength": 5.0,
        "created": now_iso,
        "source": "walk-141",
        "connections": ["walk-140-intellectual-humility", "sfi-calibration-paradox", "trust-calibration"],
        "summary": "Based on SFI finding (perfect calibration harms team performance), intellectual humility is not marking all uncertainties but distinguishing three reasoning confidence levels so users can properly calibrate trust. Over-marking = trust dilution. Effective marking = graded distinction.",
        "status": "active",
        "matures_at": None
    },
    {
        "id": "insight-141-3",
        "title": "Two-and-half-layer meta-cognition: L0 reasoning -> L1 self-eval -> L1.5 user monitoring",
        "type": "structural",
        "strength": 5.0,
        "created": now_iso,
        "source": "walk-141",
        "connections": ["walk-125-sge-architecture", "walk-142-skeleton-ram", "zylos-who-watches"],
        "summary": "Dreamer meta-cognition is finite recursion: L0 walk reasoning + L1 postmortem/audit + L1.5 user async monitoring. L1.5 is half-layer (not controlled by Dreamer) but provides the most critical signal. Implication: walk log format serves external monitor, not internal archive.",
        "status": "active",
        "matures_at": None
    }
]

data.extend(new_insights)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_insights)} insights. Total entries: {len(data)}")
