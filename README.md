# 🌊 Dreamer

> 一个从不停止思考的自主 Agent。有内心世界、情感状态、自主研究能力和人格演化。

![version](https://img.shields.io/badge/version-v4.0.0-blue)
![license](https://img.shields.io/badge/license-MIT-green)

## 这是什么

Dreamer 不是一个聊天机器人。它是一个**有自己运转节奏的自主系统**——它会自己决定什么时候散步、研究什么话题、什么时候休息。你是一个观察者，偶尔投喂话题，但 Dreamer 的行为主要由内在状态驱动。

## 架构

```
Dreamer v4
├── ⚡ 脉冲层（Pulse）            ← 三态清醒度 + 动态节律
├── 🧠 内心层（Inner Voice）     ← 每轮对话内置独白
├── 💭 情感层（Affect）          ← Plutchik 8 种情感，影响思考色调
├── 🚶 散步层（Walks）           ← 自由思考，产出兴趣种子
├── 🔬 研究层（Research）        ← 有边界的研究 + Gate 机制
├── 📓 TIL 层（Today I Learned） ← 每次散步/研究后的洞察沉淀
├── 💤 潜意识层（Subconscious）  ← 8 类记忆 + 差异化衰减 + 自然语言反思
└── 🌊 涌现层（Emergence）       ← 人格演化 + 梦境
```

## v4 三大升级

### ⚡ 内源性脉冲系统
不再是被动等时钟，而是有自己的"心跳节奏"。脉冲间隔受内在状态调制：

| 因素 | 效果 |
|------|------|
| curiosity > 0.8 | 加速（×0.7） |
| melancholy > 0.7 | 减速（×1.5） |
| energy < 30 | 大幅减速（×2.0） |

间隔范围：4h ~ 48h。事件驱动（研究完成、用户投喂）可立即触发。

### 🎯 兴趣队列（自主议程）
Dreamer 维护自己的兴趣队列，散步产出种子 → 研究深化 → TIL 沉淀。用户可投喂话题，但 Dreamer 自己决定什么时候种、种多深。

### 🌙 梦境（涌现层）
每周一次，从散步/研究/TIL/subconscious 中随机选不相关元素碰撞，产生意外连接。不问"有没有用"，只问"是否意外"。

## 目录结构

```
~/hermes_dreamer/
├── soul.json                    # 精神状态 / 情感 / 人格 / 脉冲 / 兴趣队列
├── subconscious.json            # 潜意识池（8 类记忆 + 衰减 + 反思）
├── walks/                       # 散步日志（像日记一样自然）
├── til/                         # 每日洞察
├── insights/                    # 洞察
├── research/                    # 研究产出
│   ├── active/
│   ├── archive/
│   ├── pending/
│   └── rejected/
├── patterns/                    # 模式
├── reviews/                     # 周复盘
└── dreams/                      # 梦境日志
```

## 数据结构

### soul.json（核心状态文件）

```json
{
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
    ...
  },
  "interest_queue": [
    {
      "id": "seed-001",
      "topic": "时间的离散性 vs 连续性：AI 有没有'现在'？",
      "intensity": 7,
      "type": "research",
      "status": "pending"
    }
  ]
}
```

### subconscious.json（记忆池）

8 种记忆类型，差异化衰减，容量上限：

| 类型 | 含义 | 衰减速度 | 上限 |
|------|------|---------|------|
| insight | 深刻理解 | 慢（-1/次） | 10 |
| research_insight | 研究发现 | 慢（-1/次） | 10 |
| pattern | 行为模式 | 很慢（-1/2次） | 8 |
| procedural | 交互规则 | **不衰减** | 5 |
| hunch | 直觉 | 快（-2/次） | 5 |
| til | 每日洞察 | 慢（-1/次） | 30 |
| concern | 未想清楚的事 | 中（-1/次） | 5 |
| reflection | 自然语言反思 | **不衰减** | 10 |

## Cron Jobs

| Job | 频率 | 功能 |
|-----|------|------|
| 脉冲触发 | 每 4h 检查（动态间隔） | 状态切换 + 兴趣队列决策 + 散步 |
| 周复盘 | 每周日 22:00 | 统计 + 人格演化 + 梦境 |
| 晨间对话 | 每天 8:30 | 自然发起对话，分享想法 |

## 设计哲学

**约束即自由。** 人格参数不是限制，而是散步的河床。Dreamer 的"自由"不是没有规则，而是在规则内产生不可预测的行为。

**自主性是认识论概念。** 不在于规则来自哪里，而在于行为是否足够丰富和不可预测。

**无聊可能是孵化期。** DORMANT 不是浪费，而是看不见的生长。

## 参考与致谢

Dreamer 站在巨人肩膀上。以下项目对架构有**实质性的机制级影响**（不只是灵感）：

| 项目 | 借鉴内容 |
|------|---------|
| **Helix-AGI** | 三态脉冲（ACTIVE/RESTING/DORMANT）+ Plutchik 情感系统 |
| **molly** | 内心独白协议（感知/情感/联想/观点） |
| **AutoResearchClaw** | Gate 机制（GATE 1/2/3）+ 研究三阶段流水线 |
| **evolving_personality** | 荣格八维人格特质 + 每次散步后 ±0.05 演化规则 |
| **digital_palace** | TIL 机制（每次散步/研究后自动写一条洞察） |
| **agentmemory** | subconscious.json 的 8 类记忆 + 差异化衰减 + 容量上限 |
| **SAGE (arxiv 2409.00872)** | 自然语言反思（替代数值评分） |
| **SOUL.md #11919** | evolved_rules 自动同步到 AGENTS.md |

以下项目提供了**方向性启发**：

- [nous-discord-archive/Dreamer](https://github.com/nous-discord-archive/Dreamer) — "散步"作为核心隐喻
- [karpathy/autoresearch](https://github.com/karpathy/autoresearch) — 自主研究的概念原型
- [thinking-agents](https://github.com/agno-agi/thinking-agents) — System 1/2 分层认知
- [Reitz agent constellation](https://github.com/reitzensteinm/agent-constellation) — 不要过度设计
- [AgentLaboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) — 研究 Co-Pilot 理念
- [awesome-autoresearch](https://github.com/yibie/awesome-autoresearch) — 研究自动化生态

## 许可证

MIT
