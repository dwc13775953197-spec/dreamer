#!/usr/bin/env python3
"""
Dreamer 控制操作：调整 soul.json 脉冲参数
目标：降低压力、提高阈值、切换模式、加速衰减
"""
import json
import pathlib

SOUL_PATH = pathlib.Path.home() / "hermes_dreamer" / "soul.json"

def adjust_pulse():
    with open(SOUL_PATH, "r", encoding="utf-8") as f:
        soul = json.load(f)

    pulse = soul.get("pulse", {})

    # 记录原始值用于日志
    old_pressure = pulse.get("cognitive_pressure", 70.0)
    old_threshold = pulse.get("pressure_threshold", 60.0)
    old_decay = pulse.get("decay_adjustment", 1.0)

    # 1. 压力从 70.0 降到 50.0
    pulse["cognitive_pressure"] = 50.0

    # 2. 阈值从 60.0 调整到 55.0（避免频繁触发）
    pulse["pressure_threshold"] = 55.0

    # 3. 切换为分析模式
    pulse["next_action"] = "walk_analyze"

    # 4. 衰减调整从 1.0 调到 1.2
    pulse["decay_adjustment"] = 1.2

    soul["pulse"] = pulse

    with open(SOUL_PATH, "w", encoding="utf-8") as f:
        json.dump(soul, f, indent=2, ensure_ascii=False)

    # 输出修改摘要
    print(f"压力: {old_pressure} -> {pulse['cognitive_pressure']}")
    print(f"阈值: {old_threshold} -> {pulse['pressure_threshold']}")
    print(f"next_action: -> {pulse['next_action']}")
    print(f"decay_adjustment: {old_decay} -> {pulse['decay_adjustment']}")

if __name__ == "__main__":
    adjust_pulse()
