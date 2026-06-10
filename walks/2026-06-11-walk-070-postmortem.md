# 散步 070 事后反思

## 最弱一环

「DORMANT 衰减速率 > walk 产出速率」这个断言缺少定量证据。169 条 decayed entries 的积累可能跨越了很长时间（49 次散步 + 多次 DORMANT 周期），而每次 DORMANT 的衰减量可能很小。没有精确计算就下结论，重蹈 walk-069 的覆辙。

## 前提检验

- **前提 1**：subconscious entries=0 = 枯竭 → 成立，数据清楚
- **前提 2**：DORMANT 衰减是主要原因 → 部分成立，但 entries 列表为空也可能是 schema 漂移所致（entries 字段可能是旧格式，新条目存储在其他字段中如 walk_069_insights）
- **前提 3**：walk-068 的过成熟诊断是误诊 → **不成立**——过成熟和枯竭可以同时存在于不同层面，不是互斥的
- **前提 4**：decayed 条目是「死掉的」→ 需要验证——decayed 可能只是低 strength，不一定代表认知价值为零

## 替代解释

- **Schema 漂移**：entries=0 可能意味着 subconscious.json 的存储格式变了（从 entries 数组变为 walk_xxx_insights 等独立字段），而不是真的没有活跃条目。169 条 decayed entries 是旧格式的残留。
- **正常淘汰**：169 条 decayed entries 可能是正常的认知新陈代谢——旧的不相关的 insight 被清除，为新的腾空间。entries=0 可能意味着「当前没有需要关注的活跃条目」，而不是危机。
- **walk-068 的正确性**：过成熟和枯竭可能同时存在——骨架过成熟（pattern 层）+ 潜意识枯竭（entry 层），两个问题需要不同解法。

## 知识盲区

- subconscious.json 的 schema 演变——entries 数组什么时候被废弃的？新的条目存储在哪里？
- DORMANT 衰减的具体实现——每次衰减多少条目？是否有最低水位保护？
- 「回灌」机制在认知科学中的对应物——记忆复活（memory reinstatement）在神经科学中有相关研究吗？
