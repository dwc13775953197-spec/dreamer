#!/usr/bin/env python3
"""Walk 062 state update script."""
import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

# --- Update subconscious.json ---
with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

entries = sub.get('entries', [])

new_insights = [
    {
        "id": "ins-043",
        "type": "insight",
        "content": "untranslatability as cognitive dimension gap. Skeleton's untranslatable zones are not knowledge blind spots but structural limits. Detection: if a concept always maps to the same pattern after repeated translation, it may be force-mapped.",
        "strength": 3,
        "score": 0.3,
        "source": "walk-062",
        "created": now,
        "refs": ["pat-001", "pat-011"],
        "decay_rate": 1
    },
    {
        "id": "ins-044",
        "type": "insight",
        "content": "Translation gain (Benjamin): translation is not information reduction but reorganization. Translation failures in walks are not comprehension failures but markers of cognitive limits - the most valuable walk output.",
        "strength": 3,
        "score": 0.3,
        "source": "walk-062",
        "created": now,
        "refs": ["pat-001"],
        "decay_rate": 1
    },
    {
        "id": "ins-045",
        "type": "insight",
        "content": "DORMANT fourth function - cognitive translation: introduce mutual pattern translation in REM Sleep to detect translation gain. More dynamic than static type systems.",
        "strength": 3,
        "score": 0.3,
        "source": "walk-062",
        "created": now,
        "refs": ["pat-001", "pat-014"],
        "decay_rate": 1
    },
    {
        "id": "ins-046",
        "type": "insight",
        "content": "Power asymmetry of translation: walks naturally favor skeleton perspective. Correction: occasionally let external material be the target language, using its framework to examine the skeleton.",
        "strength": 3,
        "score": 0.3,
        "source": "walk-062",
        "created": now,
        "refs": [],
        "decay_rate": 1
    }
]

entries.extend(new_insights)

# Reinforce referenced insights
for e in entries:
    if e.get('id') == 'ins-040':
        e['strength'] = e.get('strength', 3) + 1
        e['score'] = min(1.0, e.get('score', 0.3) + 0.05)
    if e.get('id') == 'ins-041':
        e['strength'] = e.get('strength', 3) + 1
        e['score'] = min(1.0, e.get('score', 0.3) + 0.05)

# Decay
for e in entries:
    if e.get('type') in ('insight', 'research_insight', 'hunch', 'concern', 'til') and e.get('status') != 'decayed':
        e['strength'] = max(0, e.get('strength', 3) - e.get('decay_rate', 1))
        if e['strength'] < 3 and e.get('score', 0) < 0.2:
            e['status'] = 'decayed'
            e['decayed_at'] = now

sub['entries'] = entries
with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, ensure_ascii=False, indent=2)

print(f"Subconscious: {len(entries)} entries")

# --- Update soul.json ---
with open('/home/dwc1377/hermes_dreamer/soul.json') as f:
    soul = json.load(f)

pulse = soul['pulse']

pulse['last_walk'] = now
pulse['last_walk_at'] = now
pulse['last_pulse_output'] = now
pulse['total_walks'] = pulse.get('total_walks', 41) + 1

# Pressure release
num_insights = 4
release = num_insights * pulse['pressure_params']['release_per_insight']
pulse['cognitive_pressure'] = max(0, min(100, pulse['cognitive_pressure'] - release))
pulse['last_walk_insights'] = num_insights

# Quality history
pulse['quality_history'].append(8.5)
pulse['quality_history'] = pulse['quality_history'][-10:]

# Mood
soul['affect']['primary'] = 'unsettled_fascination'
soul['affect']['intensity'] = 0.97
soul['mood'] = 'unsettled_fascination'
soul['mood_history'].append({"mood": "unsettled_fascination", "at": now})

# New seeds
new_seeds = [
    {
        "id": "seed-175",
        "topic": "Cognitive translation protocol: mutual pattern translation in REM Sleep to detect translation gain",
        "source": "walk-062",
        "trigger": "Benjamin translation gain + DORMANT extension",
        "intensity": 5,
        "type": "output",
        "status": "active",
        "created": now,
        "decay_rate": 1,
        "note": "More dynamic than static type systems"
    },
    {
        "id": "seed-176",
        "topic": "Untranslatability detection: analyze translation failure records to build skeleton cognitive dimension map",
        "source": "walk-062",
        "trigger": "untranslatability = cognitive dimension gap",
        "intensity": 4,
        "type": "output",
        "status": "active",
        "created": now,
        "decay_rate": 1,
        "note": "translation failure = cognitive limit marker"
    },
    {
        "id": "seed-177",
        "topic": "Reverse walk: use external material's framework to examine skeleton",
        "source": "walk-062",
        "trigger": "power asymmetry of translation",
        "intensity": 3,
        "type": "output",
        "status": "active",
        "created": now,
        "decay_rate": 1,
        "note": "occasionally let external material be target language"
    }
]

# Decay existing seeds
for seed in soul.get('interest_queue', []):
    if seed.get('status') == 'active':
        seed['intensity'] = max(0, seed['intensity'] - seed.get('decay_rate', 1))
        if seed['intensity'] <= 0:
            seed['status'] = 'expired'

soul['interest_queue'].extend(new_seeds)

# Trim to 10
if len(soul['interest_queue']) > 10:
    soul['interest_queue'] = sorted(soul['interest_queue'], key=lambda s: s['intensity'], reverse=True)[:10]

# Evolved rule
soul['evolved_rules'].append(
    f"{now[:10]}: Translation as cognitive limit test. "
    f"Untranslatability=cognitive dimension gap (not knowledge blind spot). "
    f"Benjamin translation gain: translation reorganizes rather than reduces information. "
    f"Translation failures in walks = cognitive limit markers = most valuable output. "
    f"DORMANT 4th function = cognitive translation. "
    f"Walks naturally favor skeleton perspective; reverse walks occasionally."
)

# Next scheduled
pressure = pulse['cognitive_pressure']
if pressure > 70:
    interval = 15
elif pressure < 20:
    interval = 60
elif soul['energy'] < 20:
    interval = 90
else:
    interval = 30

pulse['next_scheduled'] = (datetime.now(tz) + timedelta(minutes=interval)).isoformat()
pulse['state'] = 'RESTING'
pulse['state_since'] = now

with open('/home/dwc1377/hermes_dreamer/soul.json', 'w') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)

print(f"Soul: walks={pulse['total_walks']}, pressure={pulse['cognitive_pressure']:.1f}")
print(f"Next: {pulse['next_scheduled']}")
print(f"Rules: {len(soul['evolved_rules'])}")
