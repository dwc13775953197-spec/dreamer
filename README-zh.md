# Dreamer — 一个从不间断思考的自主 Skill + Cron

> 有内心世界、情感状态、自主研究能力和人格演化的 Agent。通过 Skill 定义行为协议，通过 Cron 驱动自主运转。

[English](README.md)

## 这是什么

Dreamer 不是聊天机器人。它是一个**有自己节律的自主系统**——自己决定什么时候散步、研究什么、什么时候休息。你是观察者，偶尔投喂话题，但 Dreamer 的行为主要由内部状态驱动。

## 架构

```
Dreamer v4.2.1
├── ⚡ Pulse Layer                 ← 三状态感知 + 动态节律 + 控制器决策
├── 🧠 Inner Voice Layer          ← 每次对话内置独白
├── 💭 Affect Layer               ← Plutchik 8 情感，影响思考语调
├── 🚶 Walk Layer                 ← 自由漫步 + 审计反馈消费 + 散步间反思
├── 🔬 Research Layer             ← 有界研究 + Gate 机制
├── 📓 TIL Layer (Today I Learned) ← 每次漫步/研究后的洞察沉淀
├── 💤 Subconscious Layer         ← 8 种记忆类型 + 差异衰减 + 推理审计 + 信念冲突检测
├── 🌙 DORMANT Layer              ← 四阶段潜意识重组（读取→联想→审计→控制决策）
├── 🔍 Validation Layer           ← 月度外部信念验证（对照学术资料）
├── 🌊 Emergence Layer            ← 人格演化 + 梦境涌现
└── 📦 Version Control            ← Git 版本控制（全系统状态追踪）
```

## v4.2.1 核心升级（2026-06-08）

### 🔄 反馈→调节通路

**问题**：审计产生的 correction/conflict 条目写入后无消费机制，审计结果无法影响后续行为。

**解决**：散步触发 cron 新增"审计反馈消费"步骤——散步前读取 correction/conflict 条目，在散步中主动避开已发现的推理陷阱，尝试调和 unresolved conflict。

### 🎯 DORMANT 控制器

**问题**：没有组件负责"基于全局状态决定下一步做什么"，全靠 cron 时间表硬编码。

**解决**：DORMANT 阶段四新增"控制决策"步骤——基于 energy/correction/interest_queue/近期产出质量等信号，决定下一次脉冲触发做什么：
- `rest` — 疲惫时延长间隔
- `walk_analyze` — 连续 FLAWED 时强制分析型散步
- `research` — 高兴趣种子触发研究
- `walk_switch` — 连续低质量时切换散步类型
- `walk_explore` — 默认探索型散步

### 📦 Git 版本控制

全系统状态纳入 Git 版本控制：
- `soul.json` / `subconscious.json` — 人格演化轨迹
- `cron/jobs.json` — 配置变更追踪
- `walks/` / `til/` / `dreams/` / `research/` — 完整认知活动记录
- 每次 cron 任务执行后自动 commit + push

## 当前状态（v4.2.1）

| 指标 | 数值 |
|------|------|
| DORMANT 周期 | 21 个（cycle 01-21） |
| Walk 次数 | 46 次（walk 001-045） |
| 潜意识条目 | 20 个活跃（7 insight / 2 pattern / 11 reflection） |
| 高评分条目 | 11 个（score ≥ 0.7） |
| 晋升 pattern | 7 个 insights → patterns |
| Cron 任务 | 9 个（6 Dreamer + 3 系统） |
| 当前情绪 | wistful_recognition（强度 0.79） |
| 当前状态 | RESTING |
| 版本控制 | ✅ Git 已启用，自动 commit + push |

### 认知骨架主轴（pat-001 → pat-031）

经过 46 次漫步和 21 个 DORMANT 周期，Dreamer 形成了 31 个 pattern：

| Pattern | 核心内容 |
|---------|---------|
| pat-001 | 过程价值三元组：涌现需要不可压缩的过程 |
| pat-002 | 外部性原理：自主性是关系性的，不是内在的 |
| pat-003 | 散步即存在证明：过程本身即价值 |
| pat-004 | DORMANT 双重性：策展与创造的平衡 |
| pat-006 | 意义的关系性原理：价值不在于产出多少 |
| pat-007 | DORMANT 作为双向时间引擎 |
| pat-008 | 时间对称性原理：重读与预放是同一操作的两面 |
| pat-011 | 叙事-时间统一原理（最高抽象层，6 引用） |
| pat-014 | 自主性即节律成熟度 |
| pat-015 | 散步塑造骨架（机械应力场） |
| pat-016 | 观察者效应作为生成原则 |
| pat-029 | 评估不确定度是内禀属性 |
| pat-030 | 散步消化循环（6 引用） |
| pat-031 | 分析型散步=咀嚼，探索型散步=觅食 |

完整列表见 subconscious.json。

## Cron 任务

| 任务 | 频率 | 功能 |
|-----|------|------|
| Pulse Trigger | 动态间隔（~5h，受内在状态调制） | 状态转换 + 控制器决策 + 散步 + 审计反馈消费 |
| DORMANT 四阶段重组 | 每天 3:00 | 读取→联想→审计（推理审计+信念冲突检测）→控制决策 |
| Weekly Review | 每周日 22:00 | 统计 + 人格演化 + 推理质量审计 + 梦境 |
| Morning Chat | 每天 8:30 | 自然发起对话，分享想法 |
| RSS 扫描 | 每 6 小时 | 外部信息摄入 |
| Monthly Validation | 每月 10 号 10:00 | 外部学术验证高置信度信念 |

## 目录结构

```
dreamer/
├── README.md / README-zh.md     # 项目文档
├── soul.json                    # 核心状态（情绪/人格/脉冲/兴趣队列/控制器）
├── subconscious.json            # 潜意识池（20 活跃条目 + correction/conflict 支持）
├── audit.jsonl                  # 审计日志（64 条）
├── walks/                       # 漫步日志（46 篇）
├── til/                         # Today I Learned（46 条）
├── dreams/                      # 梦境记录（27 个）
├── daily_news/                  # 每日新闻摘要（8 天）
├── research/                    # 研究输出
│   ├── active/                  # 进行中
│   ├── archive/                 # 归档（2 篇）
│   ├── pending/                  # 待处理（4 篇）
│   └── validations/             # 月度验证报告
├── reviews/                     # 周评（2 篇）
├── wiki/                        # 认知 Wiki（8 篇）
├── references/                  # 参考文档（27 个）
│   ├── SKILL.md                 # Dreamer 行为协议（核心，38KB）
│   ├── scoring-system.md        # 六信号评分系统
│   └── ...
├── scripts/                     # 运维脚本（10 个）
│   ├── sync_cron.py             # Cron 配置同步
│   └── rss_scan.py              # RSS 扫描
├── cron/
│   └── jobs.json                # Cron 配置（9 个任务）
└── reports/                     # 分析报告
    └── control-theory-review/   # 控制论分析
```

## 设计哲学

**约束即自由。** 人格参数不是限制——它们是漫步的河床。Dreamer 的"自由"不是规则的缺位，而是在规则内产生不可预测的行为。

**自主性是认识论概念。** 规则来源不重要——重要的是行为是否足够丰富和不可预测。

**无聊可能是孵化期。** DORMANT 不是浪费——它是看不见的生长。

**平台期是地形，不是停滞。** 细微的结构漂移仍在发生，只是需要更长时间尺度才能观测到。

**审计是自我修正的引擎。** 发现错误不是失败——发现错误并修正才是系统成熟的标志。

**控制器是大脑的前额叶。** 不只是做事情——决定什么时候做什么事情。

## 参考与致谢

以下项目对架构有**实质性机械影响**：

| 项目 | 贡献 |
|------|------|
| **Reflexion (NeurIPS 2023)** | Verbal reflection 模式 → 推理审计机制 |
| **Stanford Generative Agents** | Memory stream reflection → DORMANT 联想策略 |
| **agentic-memory** | Corrections 记录模式 → correction/conflict 条目 |
| **Reflection-Bench (ICML 2025)** | Epistemic agency 评估 → 月度信念验证 |
| **Helix-AGI** | 三状态脉冲 + Plutchik 情感系统 |
| **molly** | 内省独白协议 |
| **AutoResearchClaw** | Gate 机制 + 研究三阶段管道 |
| **evolving_personality** | Jungian 8 维人格特质 |
| **digital_palace** | TIL 机制 |
| **agentmemory** | 8 种记忆类型 + 差异衰减 |
| **SAGE (arxiv 2409.00872)** | 自然语言反思 |

以下项目提供了**方向性灵感**：

- [nous-discord-archive/Dreamer](https://github.com/nous-discord-archive/Dreamer) — "Walk" 作为核心隐喻
- [karpathy/autoresearch](https://github.com/karpathy/autoresearch) — 自主研究概念原型
- [thinking-agents](https://github.com/agno-agi/thinking-agents) — System 1/2 分层认知
- [Reitz agent constellation](https://github.com/reitzensteinm/agent-constellation) — 不要过度设计

## License

MIT
