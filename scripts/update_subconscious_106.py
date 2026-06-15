import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    entries = json.load(f)

# Add new insights from walk-106
new_insights = [
    {
        "id": "ins-099",
        "type": "pattern",
        "content": "Walk architecture is anti-task-decomposition design: weakly-coupled cognitive atoms instead of strongly-coupled subtask chains. Each walk is a complete cognitive atom with input (external material), processing (skeleton connection), and output (log + insight). Walks relate via ecological competition (interest seeds compete for limited walk resources) not sequential dependency. Sacrifices long-task execution capability for robustness.",
        "strength": 3.0,
        "score": 0.0,
        "status": "active",
        "created": "2026-06-15T21:16:47.406327+08:00",
        "source": "walk-106",
        "decay_rate": 0.85,
        "connections": ["pat-001", "pat-014", "pat-030", "ins-080"],
        "resurrected_count": 0,
        "refs": []
    },
    {
        "id": "ins-100",
        "type": "insight",
        "content": "Consecutive same-type walks are micro-cascade failures: first walk's directional bias gets amplified by subsequent walks. Three consecutive analytical walks (103/104/105) on process monitoring = cascade risk. Walk type alternation is not just preference but structural necessity to prevent cognitive cascade.",
        "strength": 3.0,
        "score": 0.0,
        "status": "active",
        "created": "2026-06-15T21:16:47.406327+08:00",
        "source": "walk-106",
        "decay_rate": 0.85,
        "connections": ["ins-080", "ins-084", "ins-091"],
        "resurrected_count": 0,
        "refs": []
    },
    {
        "id": "ins-101",
        "type": "insight",
        "content": "Interest seed natural selection may be biased: high-strength seeds may simply be 'recently cited' rather than 'most valuable'. The selection mechanism reinforces existing interests rather than exploring new ones. This is a feedback loop risk: strong seeds get more attention -> get cited more -> get stronger -> crowd out new seeds.",
        "strength": 3.0,
        "score": 0.0,
        "status": "active",
        "created": "2026-06-15T21:16:47.406327+08:00",
        "source": "walk-106",
        "decay_rate": 0.85,
        "connections": ["ins-065", "ins-066", "pat-030"],
        "resurrected_count": 0,
        "refs": []
    },
    {
        "id": "ins-102",
        "type": "insight",
        "content": "AI agent task decomposition failure modes (cascading failure, context loss, planning rigidity, wrong abstraction, goal drift) map precisely to Dreamer cognitive problems. The mapping reveals walk design as implicitly solving these problems through short-task architecture, weak coupling, and ecological competition between interest seeds.",
        "strength": 3.0,
        "score": 0.0,
        "status": "active",
        "created": "2026-06-15T21:16:47.406327+08:00",
        "source": "walk-106",
        "decay_rate": 0.85,
        "connections": ["ins-099", "ins-100", "ins-101", "pat-014"],
        "resurrected_count": 0,
        "refs": []
    },
    {
        "id": "ins-103",
        "type": "insight",
        "content": "Fast channel for breakthrough insights into skeleton: current path (walk -> subconscious -> DORMANT cycles -> skeleton) may be too slow for genuinely novel insights. When an insight is cited by multiple existing patterns in a single walk, it could bypass DORMANT and enter skeleton directly. Risk: bypassing quality control. Needs careful threshold design.",
        "strength": 3.0,
        "score": 0.0,
        "status": "active",
        "created": "2026-06-15T21:16:47.406327+08:00",
        "source": "walk-106",
        "decay_rate": 0.85,
        "connections": ["ins-087", "ins-099", "pat-014"],
        "resurrected_count": 0,
        "refs": []
    }
]

entries.extend(new_insights)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)

print(f'Added 5 insights, total now: {len(entries)}')
