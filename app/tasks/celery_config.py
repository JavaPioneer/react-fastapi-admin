#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Celery 任务注册中心

任务模块、路由与周期调度在此登记（骨架默认为空，业务项目按需追加）。

新增任务模块时在 TASK_MODULES 登记模块路径，并按需补充 TASK_ROUTES 或 BEAT_SCHEDULE：
- TASK_MODULES：填写 Python 模块完整路径，celery_app 会立即导入使 @celery_app.task 注册；
  只写路由或计划不会自动导入任务模块。
- TASK_ROUTES：键须匹配 @celery_app.task(name=...) 声明的任务名（支持末尾 * 通配符）；
  值中的 queue 必须是 settings.CELERY_QUEUES 启用的队列，未配置路由的任务走 default。
- BEAT_SCHEDULE：每个键是唯一计划标识；task 须为已注册任务的完整名。部署时只运行一个
  beat 实例，避免同一周期任务被重复投递。

Author: bixuejun(bxjgood@163.com)
Date: 2026-09-27 10:03:11  # 北京时间 UTC+8
"""

# 任务模块注册清单（当前为空骨架）
TASK_MODULES = ()

# 任务路由（当前为空骨架）
TASK_ROUTES = {}

# 周期计划（当前为空骨架）
BEAT_SCHEDULE = {}
