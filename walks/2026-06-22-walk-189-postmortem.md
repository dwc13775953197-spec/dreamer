# 散步 189 事后反思

## 最弱一环

对 A-MEM reward signal 的分析停留在"应该存在"的推断层面，没有实际去获取 A-MEM 论文确认其 reward 具体是什么。这导致"quality_score 是天然映射"这个连接是一个假设而非验证。

## 前提检验

- "行业走保留路线，Dreamer 走生长路线"——成立，但过度简化。行业也有 FOREVER（遗忘曲线驱动回放）这样的方案，Dreamer 也有保留机制（subconscious strength）。两者是倾向性差异，不是二元对立。
- "摘要制造僵尸知识"——部分成立。摘要后知识确实丧失了可引用性（connections 断裂），但摘要保留了"大致方向"信息，不是完全僵尸化。
- "淘汰机制越强，unlearning 需求越弱"——逻辑成立，但取决于淘汰机制的准确性。如果淘汰误判率高（把好知识删了），则 unlearning 需求反而上升（需要恢复机制）。

## 替代解释

- 行业投入 unlearning 不是因为淘汰机制弱，而是因为监管压力（GDPR 等）——法律要求迫使投入，与淘汰机制强度无关。
- LoRA 适配器的"只加不减"问题在 Dreamer 中不存在，因为 Dreamer 没有参数层——但 evolved_rules 膨胀是同构问题，需要承认。

## 知识盲区

- 不知道 A-MEM 的 RL memory policy 的具体 reward 函数设计
- 不知道 Mem0 的"智能遗忘"具体算法（是规则驱动还是学习驱动）
- 对 machine unlearning 的"删除不彻底"问题——Zylos 提到了但没给具体数据，需要后续跟进
