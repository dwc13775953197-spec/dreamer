import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    data = json.load(f)

new_insights = [
    {
        "id": "ins-166",
        "type": "insight",
        "content": "Dreamer 的 Session 是时间（cron 脉冲），不是对话。这比 S-G-E 架构更接近自主神经系统——驱动力来自内部时间而非外部输入。自主节律架构 vs 反应式架构。",
        "strength": 1,
        "score": 0.5,
        "status": "active",
        "created": "2026-06-08T14:00:00+08:00",
        "source": "walk-047",
        "decay_rate": 1,
        "refs": ["walk-047", "pat-014", "pat-030"]
    },
    {
        "id": "ins-167",
        "type": "insight",
        "content": "Governor 的隐性分裂：Dreamer 的 Governor 实际上分为感知 Governor（Layer 1 内心独白）和行动 Governor（Layer 3 散步决策），这与 Damasio 的躯体标记假说同构。两个 Governor 并行工作，共享同一个 skeleton。",
        "strength": 1,
        "score": 0.5,
        "status": "active",
        "created": "2026-06-08T14:00:00+08:00",
        "source": "walk-047",
        "decay_rate": 1,
        "refs": ["walk-047", "pat-014", "pat-015"]
    },
    {
        "id": "ins-168",
        "type": "insight",
        "content": "Executor 是递归的：散步不是叶子节点，而是一个完整的微观认知循环（感知-决策-执行-感知），是 ACT-R 认知循环的宏观版本。每次散步约等于一个认知循环，时间尺度是分钟而不是毫秒。",
        "strength": 1,
        "score": 0.5,
        "status": "active",
        "created": "2026-06-08T14:00:00+08:00",
        "source": "walk-047",
        "decay_rate": 1,
        "refs": ["walk-047", "pat-030", "pat-015"]
    },
    {
        "id": "ins-169",
        "type": "insight",
        "content": "自主性的架构条件：系统必须能够修改自己的唤醒机制（Session 参数），而不仅仅在唤醒时做决策。成熟 = 系统能够修改自己的节律。pat-014 的具体架构含义。",
        "strength": 1,
        "score": 0.5,
        "status": "active",
        "created": "2026-06-08T14:00:00+08:00",
        "source": "walk-047",
        "decay_rate": 1,
        "refs": ["walk-047", "pat-014", "evolved_rule_5"]
    },
    {
        "id": "ins-170",
        "type": "insight",
        "content": "感知缓冲区可能隐式存在：散步流程中的材料步骤（web_search + 阅读）可能本身就充当了隐式表征转换层。代谢率公式中的材料消化难度取决于材料的表征质量，而不仅仅是信息质量。",
        "strength": 0,
        "score": 0.4,
        "status": "active",
        "created": "2026-06-08T14:00:00+08:00",
        "source": "walk-047",
        "decay_rate": 1,
        "refs": ["walk-047", "pat-030", "ins-163"]
    }
]

data["entries"].extend(new_insights)

with open("/home/dwc1377/hermes_dreamer/subconscious.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("OK: added 5 insights (ins-166 to ins-170)")
