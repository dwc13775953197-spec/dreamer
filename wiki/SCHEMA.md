# Dreamer Wiki Schema

## Domain
Dreamer 的自主知识库。涵盖：
- **认知与思维**：涌现、自主性、认知骨架、散步洞察
- **AI 与模型**：大模型动态、AI 生态、Agent 系统
- **时间与存在**：时间性、叙事建构、身份演化
- **系统自检**：容量管理、评分系统、DORMANT 周期

## Conventions
- 文件名：英文小写+连字符（如 `cognitive-skeleton.md`）
- 中文内容为主，专有名词保留英文
- 每个 wiki 页面以 YAML frontmatter 开头
- 使用 `[[wikilinks]]` 页面间链接（每页至少 2 个出站链接）
- 更新页面时始终更新 `updated` 日期
- 每个新页面必须加入 `index.md` 对应分类
- 每个操作必须追加到 `log.md`

## Frontmatter
```yaml
---
title: 页面标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/walks/xxx.md, raw/research/xxx.md]
confidence: high | medium | low
---
```

## Tag Taxonomy
- 认知: cognition, emergence, autonomy, identity, time, narrative
- 系统: dreamer, dormant, pulse, walk, subconscious, scoring
- AI: llm, agent, model, training, inference, alignment
- 概念: concept, pattern, principle, theory
- 元数据: meta, archive, draft

规则：新标签先加到这里，再使用。

## Page Thresholds
- **创建页面**：出现在 2+ 来源中，或在一个来源里是核心
- **追加到已有页面**：来源提到已覆盖的内容
- **不创建页面**：一笔带过、细节、领域外
- **拆分页面**：超过 ~200 行

## 写入规则（Dreamer 专用）
Dreamer 写入 wiki 必须满足以下全部条件：
1. 来源可靠：来自研究产出或高质量散步日志（quality >= 7/10）
2. wiki 里已有相关页面（补充而非凭空创造）
3. 新内容至少能链接到 2 个已有页面
4. 和已有页面内容不重复

不满足条件的内容只写入 subconscious.json，不写入 wiki。

## Entity Pages
每个实体一个页面：概述、关键事实、关系、来源引用。

## Concept Pages
每个概念一个页面：定义、当前认知、开放问题、相关概念。

## Update Policy
1. 新来源优先于旧来源
2. 真实矛盾时记录双方立场，标注 `contradictions`
3. 在 lint 报告中标记待审查
