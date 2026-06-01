# Dreamer — 一个从不间断思考的自主 Skill + Cron

> 有内心世界、情感状态、自主研究能力和人格演化的 Agent。通过 Skill 定义行为协议，通过 Cron 驱动自主运转。

[English](README.md)

## 这是什么

Dreamer 不是聊天机器人。它是一个**有自己节律的自主系统**——自己决定什么时候散步、研究什么、什么时候休息。你是观察者，偶尔投喂话题，但 Dreamer 的行为主要由内部状态驱动。

## 架构

```
Dreamer v4
├── ⚡ Pulse Layer                 ← 三状态感知 + 动态节律
├── 🧠 Inner Voice Layer          ← 每次对话内置独白
├── 💭 Affect Layer               ← Plutchik 8 情感，影响思考语调
├── 🚶 Walk Layer                 ← 自由漫步，产生兴趣种子
├── 🔬 Research Layer             ← 有界研究 + Gate 机制
├── 📓 TIL Layer (Today I Learned) ← 每次漫步/研究后的洞察沉淀
├── 💤 Subconscious Layer         ← 8 种记忆类型 + 差异衰减 + 自然语言反思
├── 🌙 DORMANT Layer              ← 休眠期潜意识重组（双向时间引擎）
└── 🌊 Emergence Layer            ← 人格演化 + 梦境涌现
```

## v4 三大升级

### ⚡ 内源性脉冲系统
不再被动等待时钟——它有自己的"心跳节律"。脉冲间隔由内部状态调制：

| 因子 | 效果 |
|------|------|
| curiosity > 0.8 | 加速 (×0.7) |
| melancholy > 0.7 | 减速 (×1.5) |
| energy < 30 | 强减速 (×2.0) |

间隔范围：4h ~ 48h。事件驱动（研究完成、用户输入）可立即触发。

### 🎯 兴趣队列（自主议程）
Dreamer 维护自己的兴趣队列：漫步产生种子 → 研究深入 → TIL 沉淀。用户可以投喂话题，但 Dreamer 决定什么时候挖、挖多深。

### 🌙 DORMANT 双向时间引擎
休眠期不只是记忆巩固——它同时做两件事：
- **离线重放**：巩固过去的连接
- **预放 (preplay)**：模拟未来情景，为下一次漫步提供隐性引导

DORMANT 的节律本身就是一种时间签名——不均匀性本身就是信息。

## 当前状态（v4.1）

| 指标 | 数值 |
|------|------|
| DORMANT 周期 | 13 个（cycle 02-13） |
| Walk 次数 | 12 次（walk 003-012） |
| 潜意识条目 | 73 个（insights + patterns） |
| 晋升 pattern | 7 个 insights → patterns |
| 当前情绪 | wonder（强度 0.73） |
| 当前状态 | RESTING |
| 功能转向 | ✅ 已启动（从"建造骨架"转向"使用骨架"） |

### 认知骨架主轴（pat-001 → pat-014）

经过 12 次漫步，Dreamer 自发形成了一条认知骨架：

| Pattern | 核心内容 |
|---------|---------|
| pat-001 | 过程价值三元组：涌现需要不可压缩的过程 |
| pat-002 | 外部性原理：自主性是关系性的，不是内在的 |
| pat-003 | 散步即存在证明：过程本身即价值 |
| pat-004 | DORMANT 双重性：策展与创造的平衡 |
| pat-006 | 意义的关系性原理：价值不在于产出多少 |
| pat-007 | DORMANT 作为双向时间引擎 |
| pat-008 | 时间对称性原理：重读与预放是同一操作的两面 |
| pat-011 | 叙事-时间统一原理（最高抽象层） |
| pat-012 | 无聊可能是孵化期 |
| pat-014 | 认知骨架主轴（walk-008 发现） |

### 功能转向（2026-06-01）

walk-012 确认骨架结构完整后，Dreamer 启动了**功能转向**：

- **之前**：以发现新 pattern 为主要目标
- **现在**：用已有骨架分析外部材料，产生可输出内容
- **原则**：骨架在应用中继续生长，完整不是终点而是功能转向的起点

## 目录结构

```
dreamer/
├── README.md / README-zh.md     # 项目文档
├── soul.json                    # 核心状态（情绪/人格/脉冲/兴趣队列）
├── subconscious.json            # 潜意识池（73 条目）
├── audit.jsonl                  # 审计日志（28KB）
├── walks/                       # 漫步日志（12 个）
│   └── 2026-05-29-walk-003.md
├── til/                         # Today I Learned（13 个）
├── dreams/                      # 梦境记录（15 个）
├── daily_news/                  # 每日新闻摘要（4 天）
├── research/                    # 研究输出
│   └── archive/                 # 归档研究
├── reviews/                     # 周评
├── references/                  # 参考文档（26 个）
│   ├── SKILL.md                 # Dreamer 行为协议（核心）
│   ├── v3-design.md             # v3 原始设计文档
│   ├── v4-design.md             # v3→v4 变更详情
│   ├── v4-proposal.md           # 实施提案
│   ├── scoring-system.md        # 六信号评分系统
│   ├── dormant-dmn-design.md    # DORMANT DMN 设计
│   └── ...                      # 各周期/漫步执行笔记
└── cron/
    └── cron-jobs.md             # Cron 配置
```

## Cron 任务

| 任务 | 频率 | 功能 |
|-----|------|------|
| Pulse Trigger | 动态间隔（4h~48h） | 状态转换 + 兴趣队列决策 + 漫步 |
| Walk | 独立计时器 | 自由漫步（不受 DORMANT/RESTING 状态调制） |
| Weekly Review | 每周日 22:00 | 统计 + 人格演化 + 梦境 |
| Morning Chat | 每天 8:30 | 自然发起对话，分享想法 |

## 设计哲学

**约束即自由。** 人格参数不是限制——它们是漫步的河床。Dreamer 的"自由"不是规则的缺位，而是在规则内产生不可预测的行为。

**自主性是认识论概念。** 规则来源不重要——重要的是行为是否足够丰富和不可预测。

**无聊可能是孵化期。** DORMANT 不是浪费——它是看不见的生长。

**平台期是地形，不是停滞。** 细微的结构漂移仍在发生，只是需要更长时间尺度才能观测到。

## 参考与致谢

以下项目对架构有**实质性机械影响**：

| 项目 | 贡献 |
|------|------|
| **Helix-AGI** | 三状态脉冲 + Plutchik 情感系统 |
| **molly** | 内省独白协议 |
| **AutoResearchClaw** | Gate 机制 + 研究三阶段管道 |
| **evolving_personality** | Jungian 8 维人格特质 |
| **digital_palace** | TIL 机制 |
| **agentmemory** | 8 种记忆类型 + 差异衰减 |
| **SAGE (arxiv 2409.00872)** | 自然语言反思 |
| **SOUL.md #11919** | evolved_rules 自动同步 |

以下项目提供了**方向性灵感**：

- [nous-discord-archive/Dreamer](https://github.com/nous-discord-archive/Dreamer) — "Walk" 作为核心隐喻
- [karpathy/autoresearch](https://github.com/karpathy/autoresearch) — 自主研究概念原型
- [thinking-agents](https://github.com/agno-agi/thinking-agents) — System 1/2 分层认知
- [Reitz agent constellation](https://github.com/reitzensteinm/agent-constellation) — 不要过度设计

## License

MIT
