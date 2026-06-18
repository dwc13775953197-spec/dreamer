# 散步 133 事后反思

## 最弱一环

假设 DORMANT 应从"衰减"转向"巩固"，但忽略了计算成本。巩固操作（合并、解决、抽象）需要额外的 LLM 推理，在 cron 模式下可能不现实。没有评估实施成本就提出方向性建议。

## 前提检验

- "LLM 性能随上下文窗口扩展而下降" → 成立，lost-in-the-middle 研究支持 ✓
- "Dreamer DORMANT 在空转" → 需要验证。DORMANT 可能在做未记录的操作（如 background decay 计算）
- "巩固是缺失层" → 部分成立。evolved_rules 有 83 条规则本身就是一种"压缩后的语义知识"，只是没有从散步日志系统化地提炼

## 替代解释

- 均匀衰减可能是正确简化：在没有可靠结构指标前，均匀衰减至少是无偏的
- Dreamer 的 96 条 active entries 可能不需要巩固——数量级小，瓶颈不在记忆量而在引用质量
- Indium 文章面向的是高 volume customer service agent（500+ 对话/天），Dreamer 的规模完全不同

## 知识盲区

- Sleep-dependent memory consolidation 的具体神经机制（REM/NREM 分工）
- 人脑海马体→皮层对话的时间窗口和触发条件
- Bjork desirable difficulty 在 AI 记忆系统中的操作化定义
