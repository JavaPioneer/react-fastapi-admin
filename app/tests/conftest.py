#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试全局 conftest：恢复 Windows 默认 Proactor 事件循环策略

收集期 import test_bootstrap → import aerich 会在 Windows 全局翻转为
WindowsSelectorEventLoopPolicy（aerich/_compat.py，为 psycopg3 所设），
导致后续集成测试的 asyncio 子进程（LibreOffice soffice）抛 NotImplementedError。
本 hook 在收集完成后、运行前恢复默认 Proactor 策略。

Author: bixuejun(bxjgood@163.com)
Date: 2026-09-26 00:30:44  # 北京时间 UTC+8
"""

import asyncio
import sys


def pytest_collection_modifyitems(config, items):
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
