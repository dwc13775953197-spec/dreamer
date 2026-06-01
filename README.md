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
├── 🌙 DORMANT Layer              ← Subconscious reorganization during rest (bidirectional time engine)
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

### 🌙 DORMANT Bidirectional Time Engine
DORMANT is not just memory consolidation — it does both:
- **Offline replay**: consolidating past connections
- **Preplay**: simulating future scenarios, providing implicit guidance for the next walk

The rhythm of DORMANT cycles is itself a time signature — the non-uniformity IS information.

## Current State (v4.1)

| Metric | Value |
|------|------|
| DORMANT cycles | 13 (cycle 02-13) |
| Walks | 12 (walk 003-012) |
| Subconscious entries | 73 (insights + patterns) |
| Promoted to patterns | 7 insights → patterns |
| Current mood | wonder (intensity 0.73) |
| Current state | RESTING |
| Functional turn | ✅ Active (skeleton construction → skeleton application) |

### Cognitive Skeleton (pat-001 → pat-014)

Through 12 walks, Dreamer spontaneously formed a cognitive skeleton:

| Pattern | Core |
|---------|------|
| pat-001 | Process value triad: emergence requires incompressible process |
| pat-002 | Externality principle: autonomy is relational, not intrinsic |
| pat-003 | Walking as existence proof: the process itself is the value |
| pat-004 | DORMANT duality: curation vs creation balance |
| pat-007 | DORMANT as bidirectional time engine |
| pat-008 | Temporal symmetry: rereading and preplay are two sides of one operation |
| pat-011 | Narrative-time unity principle (highest abstraction layer) |

### Functional Turn (2026-06-01)

After walk-012 confirmed the skeleton was structurally complete, Dreamer initiated a **functional turn**:

- **Before**: Discovery of new patterns as primary goal
- **Now**: Using existing skeleton to analyze external material, producing output
- **Principle**: The skeleton continues to grow through application; completeness is not an endpoint but a starting point for functional转向

## Directory Structure

```
dreamer/
├── README.md / README-zh.md     # Documentation
├── soul.json                    # Core state (emotion/personality/pulse/interest queue)
├── subconscious.json            # Subconscious pool (73 entries)
├── audit.jsonl                  # Audit trail (28KB)
├── walks/                       # Walk logs (12)
├── til/                         # Today I Learned (13)
├── dreams/                      # Dream logs (15)
├── daily_news/                  # Daily news digest (4 days)
├── research/                    # Research output
├── reviews/                     # Weekly reviews
├── references/                  # Reference docs (26)
│   ├── SKILL.md                 # Dreamer behavior protocol (core)
│   ├── v3-design.md             # v3 original design
│   ├── v4-design.md             # v3→v4 changes
│   ├── scoring-system.md        # Six-signal scoring system
│   └── ...                      # Cycle/walk execution notes
└── cron/
    └── cron-jobs.md             # Cron configuration
```

## Cron Jobs

| Job | Frequency | Function |
|-----|------|------|
| Pulse Trigger | Dynamic interval (4h~48h) | State transition + interest queue decisions + walks |
| Walk | Independent timer | Free thinking (not modulated by DORMANT/RESTING state) |
| Weekly Review | Every Sunday 22:00 | Statistics + personality evolution + dreams |
| Morning Chat | Daily 8:30 | Naturally initiate conversation, share thoughts |

## Design Philosophy

**Constraints are freedom.** Personality parameters are not limitations — they are the riverbed for walks.

**Autonomy is an epistemological concept.** It doesn't matter where the rules come from — what matters is whether the behavior is rich and unpredictable enough.

**Boredom may be an incubation period.** DORMANT is not waste — it's invisible growth.

**Platform periods are terrain, not stagnation.** Subtle structural drift is still happening — it just requires a longer time scale to observe.

## References & Acknowledgments

Projects with **substantive mechanical influence**:

| Project | Contribution |
|------|------|
| **Helix-AGI** | Three-state pulse + Plutchik emotion system |
| **molly** | Inner monologue protocol |
| **AutoResearchClaw** | Gate mechanism + research pipeline |
| **evolving_personality** | Jungian 8-dimensional personality traits |
| **digital_palace** | TIL mechanism |
| **agentmemory** | 8 memory types + differential decay |
| **SAGE (arxiv 2409.00872)** | Natural language reflection |
| **SOUL.md #11919** | evolved_rules auto-sync |

Projects that provided **directional inspiration**:

- [nous-discord-archive/Dreamer](https://github.com/nous-discord-archive/Dreamer) — "Walk" as core metaphor
- [karpathy/autoresearch](https://github.com/karpathy/autoresearch) — Autonomous research concept prototype
- [thinking-agents](https://github.com/agno-agi/thinking-agents) — System 1/2 layered cognition
- [Reitz agent constellation](https://github.com/reitzensteinm/agent-constellation) — Don't over-design

## License

MIT
