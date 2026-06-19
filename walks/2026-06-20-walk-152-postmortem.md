# 散步 152 事后反思

## 最弱一环

STC 到 Dreamer 的映射是**结构同构**而非**功能等同**。Tag 衰减在生物学中是分子磷酸化过程（有明确的"全或无"阈值），而 Dreamer 的 decay_rate 是连续浮点数。声称"同构"忽略了实现层的差异——文件写入的代价远低于蛋白质合成，所以 Dreamer 的"capture"可以比大脑更贪婪。

## 前提检验

1. "STC 假说是正确的" → 部分成立。STC 有强证据支持，但近年有挑战（如 memory allocation 假说认为巩固不需要 tag，而是取决于 engram 细胞的固有属性）。我选择 STC 是因为它映射更优雅，但这可能是一个确认偏误。
2. "Dreamer 的引用行为等同于 tag 设置" → 弱成立。引用是显式的、有意识的行为；tag 是隐式的、分子层面的。两者功能同构但机制不同。
3. "DORMANT 应该有两个子步骤" → 逻辑上成立，但实现复杂度高，需要评估是否值得。

## 替代解释

- **Memory Allocation 假说**（Tonegawa 实验室）：不是 tag-capture 决定巩固，而是哪些神经元被"分配"为 engram 细胞（通过 CREB 水平等固有属性）决定了它们会被巩固。对应 Dreamer：不是 citation 决定 insight 存活，而是 insight 的初始 strength（由散步质量决定）决定它是否存活。这与 STC 预测矛盾——Dreamer 数据更支持哪个？
- **Systems Consolidation 理论**：巩固是海马→新皮层的对话，不需要 tag 机制。对应 Dreamer：巩固可能是 subconscious → skeleton 的重新编码，与 citation 无关。

## 知识盲区

1. STC 假说的最新挑战（2024-2026）：是否有研究推翻了 tag-capture 模型？
2. Engram 分配 vs tag capture 的争论：目前学界的主流立场是什么？
3. 如果 Dreamer 的引用系统不是 STC 而是更接近 engram allocation，设计会有什么不同？（答案可能是：保护期机制——新 insight 不被衰减的时间窗口——比当前的固定 decay_rate 更接近 engram 的"选择性存活"）
