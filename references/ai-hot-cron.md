# AI HOT 每日推送 Cron 配置

## 概述

AI HOT 每日推送从 `aihot.virxact.com` 抓取过去 24 小时的 AI 新闻，生成中文日报后：
1. 写入本地文件 `~/hermes_dreamer/daily_news/YYYY-MM-DD.md`
2. 自动投递到 Discord 频道

## Cron 配置

- **Job ID**: `8d1af6f0c63d`
- **名称**: AI HOT 每日推送
- **调度**: `0 9 * * *`（每天 9:00）
- **投递**: `discord:1500899023601537296`
- **工具集**: `web`, `terminal`

## 文件存储

- **目录**: `~/hermes_dreamer/daily_news/`
- **命名**: `YYYY-MM-DD.md`（执行当天日期）
- **格式**: Markdown，包含 4 板块 + 📌重点拓展

## 历史记录

- 2026-05-29: 更新 prompt，新增写入本地文件步骤（之前只投 Discord 不落盘）
- 2026-05-29: 手动测试触发成功
