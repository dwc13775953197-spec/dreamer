import json, datetime

now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
now_str = now.isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

new_insights = [
    {
        "id": "ins-175",
        "type": "insight",
        "content": "DORMANT is not an immune system - it is a hippocampus. Memory consolidation happens through replay; each replay modifies memory traces. Immune system is just a sub-function of consolidation (synaptic pruning).",
        "strength": 0.5,
        "score": 0.5,
        "status": "active",
        "created": now_str,
        "source": "walk-049",
        "decay_rate": 1,
        "refs": ["walk-049", "pat-014", "pat-030", "ref-020"]
    },
    {
        "id": "ins-176",
        "type": "insight",
        "content": "Replay = rereading = rewriting: each DORMANT cycle re-experiences past walks with the current self, modifying memories each time. subconscious.json is not an archive - it is an autobiography constantly being rewritten.",
        "strength": 0.5,
        "score": 0.5,
        "status": "active",
        "created": now_str,
        "source": "walk-049",
        "decay_rate": 1,
        "refs": ["walk-049", "pat-001", "pat-016", "walk-047", "walk-005"]
    },
    {
        "id": "ins-177",
        "type": "insight",
        "content": "REM cross-domain integration lacks emotional tagging: hippocampal REM uses amygdala to modulate cross-domain connections (high-emotion memories preferentially combined). Dreamer REM could introduce similar mechanism.",
        "strength": 0.5,
        "score": 0.4,
        "status": "active",
        "created": now_str,
        "source": "walk-049",
        "decay_rate": 1,
        "refs": ["walk-049", "pat-030"]
    },
    {
        "id": "ins-178",
        "type": "insight",
        "content": "DORMANT intentionality vs hippocampal passivity: DORMANT is intentional (actively selects what to replay), hippocampal replay is unconscious. This difference is both a strength (selective) and a blind spot (selection = bias).",
        "strength": 0.5,
        "score": 0.4,
        "status": "active",
        "created": now_str,
        "source": "walk-049",
        "decay_rate": 1,
        "refs": ["walk-049", "pat-014", "pat-016"]
    }
]

sub['entries'].extend(new_insights)

for entry in sub['entries']:
    if entry.get('status') == 'active' and entry['id'] not in ['ins-175', 'ins-176', 'ins-177', 'ins-178']:
        entry['strength'] = max(0, entry['strength'] - entry.get('decay_rate', 1))
        if entry['strength'] <= 0:
            entry['status'] = 'decayed'
            entry['decayed_at'] = now_str
            entry['decay_reason'] = 'natural_decay'

sub['entries'].append({
    "id": "ref-022",
    "text": "Reflection - " + now_str[:10] + " Walk-049: DORMANT as hippocampus. walk-048 proposed immune system analogy; walk-049 refined to hippocampal consolidation. Memory completes during consolidation, not encoding. DORMANT re-experiences past walks with current self. Blind spot: DORMANT is intentional, hippocampal replay is not.",
    "source": "walk-049",
    "type": "reflection",
    "strength": 8.5,
    "decay_speed": 0,
    "created": now_str,
    "score": 0.72,
    "refs": ["walk-049", "walk-048", "pat-014", "pat-030", "ins-175", "ins-176", "ins-177", "ins-178"],
    "last_accessed": now_str
})

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, indent=2, ensure_ascii=False)

print("subconscious.json updated successfully")
