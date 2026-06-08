#!/usr/bin/env python3
"""
Dreamer Cron 同步脚本

将 Dreamer 仓库中的 cron/jobs.json 同步到 Hermes 的 ~/.hermes/cron/jobs.json。
在 Dreamer 的 cron 任务执行完毕后自动调用。

用法：
  python3 ~/hermes_dreamer/scripts/sync_cron.py

设计思路：
  - Dreamer 仓库是 cron 配置的单一来源（single source of truth）
  - Hermes 的 ~/.hermes/cron/jobs.json 是运行时配置
  - 每次 Dreamer cron 任务修改 jobs.json 后，运行此脚本同步
  - 同步后自动 git commit Dreamer 仓库中的变更
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

DREAMER_DIR = Path.home() / "hermes_dreamer"
HERMES_CRON = Path.home() / ".hermes" / "cron" / "jobs.json"
DREAMER_CRON = DREAMER_DIR / "cron" / "jobs.json"


def sync():
    """从 Dreamer 仓库同步到 Hermes"""
    if not DREAMER_CRON.exists():
        print(f"ERROR: {DREAMER_CRON} not found")
        sys.exit(1)

    # 验证 JSON 有效
    with open(DREAMER_CRON) as f:
        data = json.load(f)

    # 备份 Hermes 当前配置
    if HERMES_CRON.exists():
        backup = HERMES_CRON.with_suffix(".json.bak")
        shutil.copy2(HERMES_CRON, backup)

    # 同步
    HERMES_CRON.parent.mkdir(parents=True, exist_ok=True)
    with open(HERMES_CRON, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Synced: {DREAMER_CRON} -> {HERMES_CRON}")
    print(f"Jobs: {len(data.get('jobs', []))}")

    # 检查变更并 git commit
    try:
        result = subprocess.run(
            ["git", "diff", "--quiet", str(DREAMER_CRON)],
            cwd=str(DREAMER_DIR),
            capture_output=True,
        )
        if result.returncode != 0:
            # 有变更，commit
            subprocess.run(
                ["git", "add", "cron/jobs.json"],
                cwd=str(DREAMER_DIR),
                check=True,
            )
            subprocess.run(
                ["git", "commit", "-m", "chore: sync cron config update"],
                cwd=str(DREAMER_DIR),
                check=True,
            )
            print("Committed cron changes to Dreamer repo")
        else:
            print("No changes to commit")
    except subprocess.CalledProcessError as e:
        print(f"Git commit failed (non-fatal): {e}")


if __name__ == "__main__":
    sync()
