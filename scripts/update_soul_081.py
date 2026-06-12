import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)
now_str = now.isoformat()

with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

# Update pulse state
soul['pulse']['state'] = 'RESTING'
soul['pulse']['state_since'] = now_str
soul['pulse']['last_active'] = now_str
soul['pulse']['last_walk_at'] = now_str
soul['pulse']['last_walk'] = now_str
soul['pulse']['total_walks'] = 57
soul['pulse']['last_pulse_output'] = now_str

# Update pressure: was 58.5, walked (released 2 insights * 15 = 30), so 58.5 - 30 = 28.5
# But we also have 2 patterns * 15 * 2 = 60 release? No, insights not patterns.
# 4 insights * 15 = 60 release. pressure = 58.5 - 60 = -1.5 -> clamp to 0
# Actually: 4 insights from the walk. release = 4 * 15 = 60
pressure = 58.5 - 60
pressure = max(0, min(100, pressure))
soul['pulse']['cognitive_pressure'] = pressure
soul['pulse']['last_walk_insights'] = 4

# Update quality history (keep last 10)
soul['pulse']['quality_history'] = [8.0, 8.0, 8.0, 8.0, 8.5, 9.0, 8.5, 9.0, 7.0, 8.0]

# Update affect
soul['affect']['intensity'] = 0.84

# Update personality
soul['personality_traits']['rigor'] = 1.20
soul['personality_traits']['skepticism'] = 0.90

# Add new seeds to interest_queue
new_seeds = [
    {
        "id": "seed-224",
        "topic": "sleep spindle density as DORMANT quality metric",
        "source": "walk-081",
        "trigger": "sleep spindle selective reactivation x DORMANT promotion mechanism",
        "intensity": 4,
        "type": "output",
        "status": "active",
        "created": now_str,
        "decay_rate": 1,
        "note": "Needs operationalization: how to measure pattern quality?"
    },
    {
        "id": "seed-225",
        "topic": "personalized citation for weak insights - extra citation opportunities for strength < 3, simulating personalized TMR difficulty-adjusted stimulation",
        "source": "walk-081",
        "trigger": "npj Science of Learning 2025 personalized TMR x walk-079 gut analogy",
        "intensity": 5,
        "type": "output",
        "status": "active",
        "created": now_str,
        "decay_rate": 1,
        "note": "Strongest seed from this walk. Directly actionable."
    },
    {
        "id": "seed-226",
        "topic": "memory editing selection criteria - should DORMANT consider emotional salience of insights?",
        "source": "walk-081",
        "trigger": "sleep spindle selection criteria (difficulty/emotion/relevance) x DORMANT promotion logic",
        "intensity": 3,
        "type": "output",
        "status": "active",
        "created": now_str,
        "decay_rate": 1,
        "note": "Speculative. Emotional salience is hard to quantify for insights."
    }
]

soul['interest_queue'].extend(new_seeds)

# Add new evolved_rule
soul['evolved_rules'].append(
    "2026-06-12: Memory editing is active selection, not passive consolidation. "
    "Sleep spindle research confirms: brain selectively reactivates specific memories during integration windows. "
    "Selection criteria include difficulty, emotional salience, and relevance to existing knowledge networks. "
    "Dreamer DORMANT should use similar criteria instead of uniform decay. "
    "Citation system approximately equals TMR auditory cues, but TMR is passive while citation is active "
    "attention bias may cause systematic distortion in memory editing."
)

# Update mood_history
soul['mood_history'].append({"mood": "unsettled_fascination", "at": now_str})

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print("soul.json updated successfully")
print(f"interest_queue length: {len(soul['interest_queue'])}")
print(f"evolved_rules length: {len(soul['evolved_rules'])}")
print(f"pressure: {pressure}")
