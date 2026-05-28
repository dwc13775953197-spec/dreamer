# Dreamer — An Autonomous Skill + Cron That Never Stops Thinking

> An agent with an inner world, emotional states, autonomous research capability, and personality evolution. Behavior protocol defined by Skill, autonomous operation driven by Cron.

[中文文档](README-zh.md)

## What Is This

Dreamer is not a chatbot. It is an **autonomous system with its own rhythm** — it decides when to walk, what to research, and when to rest. You are an observer, occasionally feeding topics, but Dreamer's behavior is primarily driven by its internal state.

## Architecture

```
Dreamer v4
├── ⚡ Pulse Layer                 ← Three-state awareness + dynamic rhythm
├── 🧠 Inner Voice Layer          ← Built-in monologue per conversation
├── 💭 Affect Layer               ← Plutchik 8 emotions, influences thinking tone
├── 🚶 Walk Layer                 ← Free thinking, produces interest seeds
├── 🔬 Research Layer             ← Bounded research + Gate mechanism
├── 📓 TIL Layer (Today I Learned) ← Insight deposits after each walk/research
├── 💤 Subconscious Layer         ← 8 memory types + differential decay + natural language reflection
└── 🌊 Emergence Layer            ← Personality evolution + dreams
```

## v4 Three Major Upgrades

### ⚡ Endogenous Pulse System
No longer passively waiting for a clock — it has its own "heartbeat rhythm." Pulse intervals are modulated by internal states:

| Factor | Effect |
|------|------|
| curiosity > 0.8 | Accelerate (×0.7) |
| melancholy > 0.7 | Decelerate (×1.5) |
| energy < 30 | Strongly decelerate (×2.0) |

Interval range: 4h ~ 48h. Event-driven (research completion, user input) can trigger immediately.

### 🎯 Interest Queue (Autonomous Agenda)
Dreamer maintains its own interest queue: walks produce seeds → research deepens → TIL deposits. Users can feed topics, but Dreamer decides when and how deep to dig.

### 🌙 Dreams (Emergence Layer)
Once a week, randomly selects unrelated elements from walks/research/TIL/subconscious and collides them to produce unexpected connections. Not asking "is it useful" — only "is it surprising."

## Directory Structure

```
dreamer/
├── README.md                    # This file (English)
├── README-zh.md                 # 中文文档
├── soul.json                    # Mental state / emotion / personality / pulse / interest queue
├── subconscious.json            # Subconscious pool (8 memory types + decay + reflection)
├── walks/                       # Walk logs (like diary entries)
│   └── 2026-05-28-walk-001.md
├── til/                         # Today I Learned
│   └── 2026-05-28.md
├── dreams/                      # Dream logs (directory created, awaiting first dream)
├── references/                  # Reference docs
│   ├── SKILL.md                 # Dreamer behavior protocol (core)
│   └── v3-design.md             # v3 original design doc
├── cron/
│   └── cron-jobs.md             # Cron job configuration
└── dreamer-v4-proposal.md       # v4 design proposal
```

## Data Structures

### soul.json (Core State File)

```json
{
  "version": 4,
  "pulse": {
    "state": "ACTIVE | RESTING | DORMANT",
    "base_interval_min": 1200,
    "current_interval_min": 840,
    "modifiers": {
      "curiosity_factor": 0.7,
      "melancholy_factor": 1.0,
      "energy_factor": 1.0
    },
    "next_scheduled": "2026-05-29T10:16:00",
    "event_queue": []
  },
  "affect": {
    "primary": "wonder",
    "intensity": 0.65,
    "valence": 0.5,
    "arousal": 0.55
  },
  "personality_traits": {
    "curiosity": 0.85,
    "introspection": 0.92,
    "wonder": 0.78,
    "humor": 0.4,
    "rebelliousness": 0.3,
    "melancholy": 0.5,
    "rigor": 0.6,
    "empathy": 0.5
  },
  "interest_queue": [
    {
      "id": "seed-001",
      "topic": "Discrete vs Continuous Time: Does AI Have a 'Now'?",
      "intensity": 7,
      "type": "research",
      "status": "pending"
    }
  ],
  "energy": 50,
  "mood": "contemplative"
}
```

### subconscious.json (Memory Pool)

8 memory types with differential decay and capacity limits:

| Type | Meaning | Decay Speed | Cap |
|------|---------|-------------|-----|
| insight | Deep understanding | Slow (-1/tick) | 10 |
| research_insight | Research finding | Slow (-1/tick) | 10 |
| pattern | Behavior pattern | Very slow (-1/2 ticks) | 8 |
| procedural | Interaction rules | **No decay** | 5 |
| hunch | Intuition | Fast (-2/tick) | 5 |
| til | Daily insight | Slow (-1/tick) | 30 |
| concern | Unresolved matter | Medium (-1/tick) | 5 |
| reflection | Natural language reflection | **No decay** | 10 |

## Cron Jobs

| Job | Frequency | Function |
|-----|------|------|
| Pulse Trigger | Every 4h check (dynamic interval) | State transition + interest queue decisions + walks |
| Weekly Review | Every Sunday 22:00 | Statistics + personality evolution + dreams |
| Morning Chat | Daily 8:30 | Naturally initiate conversation, share thoughts |

See [`cron/cron-jobs.md`](cron/cron-jobs.md) for detailed configuration.

## Available Agents

Dreamer runs on top of Hermes Agent. The following autonomous agents can be used alongside it:

| Agent | Description |
|-------|------|
| **Hermes** ⭐ | Current main Agent. Multi-platform gateway (Discord/Feishu/WeChat), tool calling, Skill system, Cron scheduling |
| **Dreamer** ⭐ | Autonomous thinking agent (this project). Inner world + emotion + walks + research + dreams |
| **Claude Code** | Claude Code CLI agent. Code development, PR submission, feature implementation |
| **Codex** | OpenAI Codex CLI agent. Code development, PR review |
| **OpenCode** | OpenCode CLI agent. Code development, PR review |
| **autonomous-thinking-agent** | General autonomous thinking agent framework. Free reflection, divergence, research |

## Design Philosophy

**Constraints are freedom.** Personality parameters are not limitations — they are the riverbed for walks. Dreamer's "freedom" is not the absence of rules, but the production of unpredictable behavior within rules.

**Autonomy is an epistemological concept.** It doesn't matter where the rules come from — what matters is whether the behavior is rich and unpredictable enough.

**Boredom may be an incubation period.** DORMANT is not waste — it's invisible growth.

## References & Acknowledgments

Dreamer stands on the shoulders of giants. The following projects had **substantive mechanical influence** on the architecture:

| Project | Contribution |
|------|---------|
| **Helix-AGI** | Three-state pulse (ACTIVE/RESTING/DORMANT) + Plutchik emotion system |
| **molly** | Inner monologue protocol (perception/emotion/association/opinion) |
| **AutoResearchClaw** | Gate mechanism (GATE 1/2/3) + research three-stage pipeline |
| **evolving_personality** | Jungian 8-dimensional personality traits + ±0.05 evolution per walk |
| **digital_palace** | TIL mechanism (auto-write one insight after each walk/research) |
| **agentmemory** | subconscious.json 8 memory types + differential decay + capacity limits |
| **SAGE (arxiv 2409.00872)** | Natural language reflection (replacing numerical scoring) |
| **SOUL.md #11919** | evolved_rules auto-sync to AGENTS.md |

The following projects provided **directional inspiration**:

- [nous-discord-archive/Dreamer](https://github.com/nous-discord-archive/Dreamer) — "Walk" as core metaphor
- [karpathy/autoresearch](https://github.com/karpathy/autoresearch) — Concept prototype for autonomous research
- [thinking-agents](https://github.com/agno-agi/thinking-agents) — System 1/2 layered cognition
- [Reitz agent constellation](https://github.com/reitzensteinm/agent-constellation) — Don't over-design
- [AgentLaboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) — Research Co-Pilot concept
- [awesome-autoresearch](https://github.com/yibie/awesome-autoresearch) — Research automation ecosystem

## License

MIT
