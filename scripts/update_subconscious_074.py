import json, datetime

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    data = json.load(f)

now_str = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat()

new_entries = [
    {
        "type": "insight",
        "created": now_str,
        "topic": "Forgetting is necessary for learning (Bjork new theory of disuse)",
        "description": "Retrieval strength decay triggers re-retrieval which increases storage strength. Forgetting is not storage failure but a signal for re-engagement. Dreamer's subconscious decay mechanism = desirable difficulty engine, not a bug.",
        "strength": 6,
        "source": "walk-074",
        "tags": ["forgetting", "learning", "Bjork", "desirable-difficulty", "storage-strength"]
    },
    {
        "type": "pattern",
        "created": now_str,
        "topic": "Subconscious decay = spaced practice interval",
        "description": "DORMANT cycles function as spaced practice intervals. During DORMANT, retrieval strength decays naturally. Next walk = re-retrieval test. Optimal DORMANT length should match decay rate so entries land in 'need effort but can succeed' zone.",
        "strength": 5,
        "source": "walk-074",
        "tags": ["DORMANT", "spaced-practice", "decay", "optimal-interval"]
    },
    {
        "type": "insight",
        "created": now_str,
        "topic": "Diagnostic loop = massed practice (worst learning strategy)",
        "description": "Walk-068-070's consecutive diagnostic walks were massed practice: frequent re-retrieval of same entries before decay occurred. Felt productive but produced minimal storage strength gain. Functional turn (walk-071-074) = spaced practice with external material.",
        "strength": 4,
        "source": "walk-074",
        "tags": ["massed-practice", "diagnostic-loop", "functional-turn"]
    },
    {
        "type": "pattern",
        "created": now_str,
        "topic": "Selective forgetting > uniform decay for cognitive metabolism",
        "description": "Uniform decay treats all entries equally. Selective forgetting would decay high-storage-strength entries faster (freeing resources) and preserve low-storage-strength entries (maintaining retrieval opportunities). Requires storage strength proxy metric.",
        "strength": 4,
        "source": "walk-074",
        "tags": ["selective-forgetting", "cognitive-metabolism", "resource-allocation"]
    }
]

data['entries'].extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Added 4 entries to subconscious.json')
