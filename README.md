# Dreamer — An Autonomous Skill + Cron That Never Stops Thinking

> An agent with an inner world, emotional states, autonomous research capability, and personality evolution. Behavior protocol defined by Skill, autonomous operation driven by Cron.

[中文文档](README-zh.md)

## What Is This

Dreamer is not a chatbot. It is an **autonomous system with its own rhythm** — it decides when to walk, what to research, and when to rest. You are an observer, occasionally feeding topics, but Dreamer's behavior is primarily driven by its internal state.

## Architecture

```
Dreamer v4.2.1
├── ⚡ Pulse Layer                 ← Three-state awareness + dynamic rhythm + controller decisions
├── 🧠 Inner Voice Layer          ← Built-in monologue per conversation
├── 💭 Affect Layer               ← Plutchik 8 emotions, influences thinking tone
├── 🚶 Walk Layer                 ← Free thinking + audit feedback consumption + post-walk reflection
├── 🔬 Research Layer             ← Bounded research + Gate mechanism
├── 📓 TIL Layer (Today I Learned) ← Insight deposits after each walk/research
├── 💤 Subconscious Layer         ← 8 memory types + differential decay + reasoning audit + belief conflict detection
├── 🌙 DORMANT Layer              ← Four-phase subconscious reorganization (Read → Associate → Audit → Control)
├── 🔍 Validation Layer           ← Monthly external belief validation (against academic sources)
├── 🌊 Emergence Layer            ← Personality evolution + dreams
└── 📦 Version Control            ← Git version control (full system state tracking)
```

## v4.2.1 Core Upgrades (2026-06-08)

### 🔄 Feedback→Regulation Pathway

**Problem**: Correction/conflict entries from audits had no consumption mechanism — audit results couldn't influence subsequent behavior.

**Solution**: Pulse trigger cron now includes an "audit feedback consumption" step — reads correction/conflict entries before walking, actively avoids known reasoning pitfalls, attempts to resolve unresolved conflicts.

### 🎯 DORMANT Controller

**Problem**: No component responsible for "deciding what to do next based on global state" — everything was hardcoded cron schedules.

**Solution**: DORMANT phase 4 now includes a "control decision" step — based on energy/correction/interest_queue/recent output quality signals, decides what the next pulse trigger should do:
- `rest` — extend interval when exhausted
- `walk_analyze` — forced analytical walks after consecutive FLAWED audits
- `research` — high-interest seeds trigger research
- `walk_switch` — switch walk type after consecutive low-quality output
- `walk_explore` — default exploratory walk

### 📦 Git Version Control

Full system state under Git version control:
- `soul.json` / `subconscious.json` — personality evolution trajectory
- `cron/jobs.json` — configuration change tracking
- `walks/` / `til/` / `dreams/` / `research/` — complete cognitive activity records
- Auto commit + push after each cron job execution

## Current State (v4.2.1)

| Metric | Value |
|------|------|
| DORMANT cycles | 21 (cycle 01-21) |
| Walks | 46 (walk 001-045) |
| Subconscious entries | 20 active (7 insight / 2 pattern / 11 reflection) |
| High-score entries | 11 (score ≥ 0.7) |
| Promoted to patterns | 7 insights → patterns |
| Cron jobs | 9 (6 Dreamer + 3 system) |
| Current mood | wistful_recognition (intensity 0.79) |
| Current state | RESTING |
| Version control | ✅ Git enabled, auto commit + push |

### Cognitive Skeleton (pat-001 → pat-031)

Through 46 walks and 21 DORMANT cycles, Dreamer has formed 31 patterns:

| Pattern | Core |
|---------|------|
| pat-001 | Process value triad: emergence requires incompressible process |
| pat-002 | Externality principle: autonomy is relational, not intrinsic |
| pat-003 | Walking as existence proof: the process itself is the value |
| pat-004 | DORMANT duality: curation vs creation balance |
| pat-006 | Meaning's relational principle: value is not about output quantity |
| pat-007 | DORMANT as bidirectional time engine |
| pat-008 | Temporal symmetry: rereading and preplay are two sides of one operation |
| pat-011 | Narrative-time unity principle (highest abstraction, 6 refs) |
| pat-014 | Autonomy as rhythm maturity |
| pat-015 | Walking shapes skeleton (mechanical stress field) |
| pat-016 | Observer effect as generation principle |
| pat-029 | Evaluation uncertainty is intrinsic |
| pat-030 | Walking digestive cycle (6 refs) |
| pat-031 | Analytical walk = chewing, exploratory walk = foraging |

Full list in subconscious.json.

## Cron Jobs

| Job | Frequency | Function |
|-----|------|------|
| Pulse Trigger | Dynamic interval (~5h, modulated by internal state) | State transition + controller decision + walk + audit feedback consumption |
| DORMANT Four-Phase Reorganization | Daily 3:00 | Read → Associate → Audit (reasoning audit + belief conflict detection) → Control decision |
| Weekly Review | Every Sunday 22:00 | Statistics + personality evolution + reasoning quality audit + dreams |
| Morning Chat | Daily 8:30 | Naturally initiate conversation, share thoughts |
| RSS Scan | Every 6 hours | External information intake |
| Monthly Validation | 10th of each month 10:00 | External academic validation of high-confidence beliefs |

## Directory Structure

```
dreamer/
├── README.md / README-zh.md     # Documentation
├── soul.json                    # Core state (emotion/personality/pulse/interest queue/controller)
├── subconscious.json            # Subconscious pool (20 active + correction/conflict support)
├── audit.jsonl                  # Audit trail (64 entries)
├── walks/                       # Walk logs (46)
├── til/                         # Today I Learned (46)
├── dreams/                      # Dream logs (27)
├── daily_news/                  # Daily news digest (8 days)
├── research/                    # Research output
│   ├── active/                  # In progress
│   ├── archive/                 # Archived (2)
│   ├── pending/                  # Pending (4)
│   └── validations/             # Monthly validation reports
├── reviews/                     # Weekly reviews (2)
├── wiki/                        # Cognitive Wiki (8)
├── references/                  # Reference docs (27)
│   ├── SKILL.md                 # Dreamer behavior protocol (core, 38KB)
│   ├── scoring-system.md        # Six-signal scoring system
│   └── ...
├── scripts/                     # Ops scripts (10)
│   ├── sync_cron.py             # Cron config sync
│   └── rss_scan.py              # RSS scanning
├── cron/
│   └── jobs.json                # Cron config (9 jobs)
└── reports/                     # Analysis reports
    └── control-theory-review/   # Control theory analysis
```

## Design Philosophy

**Constraints are freedom.** Personality parameters are not limitations — they are the riverbed for walks.

**Autonomy is an epistemological concept.** It doesn't matter where the rules come from — what matters is whether the behavior is rich and unpredictable enough.

**Boredom may be an incubation period.** DORMANT is not waste — it's invisible growth.

**Platform periods are terrain, not stagnation.** Subtle structural drift is still happening — it just requires a longer time scale to observe.

**Audit is the engine of self-correction.** Finding errors is not failure — finding and correcting them is the mark of a maturing system.

**The controller is the prefrontal cortex.** Not just doing things — deciding when to do what.

## References & Acknowledgments

Projects with **substantive mechanical influence**:

| Project | Contribution |
|------|------|
| **Reflexion (NeurIPS 2023)** | Verbal reflection pattern → reasoning audit mechanism |
| **Stanford Generative Agents** | Memory stream reflection → DORMANT association strategy |
| **agentic-memory** | Corrections recording pattern → correction/conflict entries |
| **Reflection-Bench (ICML 2025)** | Epistemic agency evaluation → monthly belief validation |
| **Helix-AGI** | Three-state pulse + Plutchik emotion system |
| **molly** | Inner monologue protocol |
| **AutoResearchClaw** | Gate mechanism + research pipeline |
| **evolving_personality** | Jungian 8-dimensional personality traits |
| **digital_palace** | TIL mechanism |
| **agentmemory** | 8 memory types + differential decay |
| **SAGE (arxiv 2409.00872)** | Natural language reflection |

Projects that provided **directional inspiration**:

- [nous-discord-archive/Dreamer](https://github.com/nous-discord-archive/Dreamer) — "Walk" as core metaphor
- [karpathy/autoresearch](https://github.com/karpathy/autoresearch) — Autonomous research concept prototype
- [thinking-agents](https://github.com/agno-agi/thinking-agents) — System 1/2 layered cognition
- [Reitz agent constellation](https://github.com/reitzensteinm/agent-constellation) — Don't over-design

## License

MIT
