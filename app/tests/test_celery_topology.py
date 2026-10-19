#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Celery 队列拓扑与 beat 调度测试

Author: bixuejun(bxjgood@163.com)
Date: 2026-09-24 15:14:00  # 北京时间 UTC+8
"""

from app.celery.celery_app import celery_app
from app.settings import settings


class TestQueueTopology:
    def test_default_queue_only(self) -> None:
        queue_names = {q.name for q in celery_app.conf.task_queues}
        assert queue_names == {"default"}

    def test_queues_follow_settings(self) -> None:
        assert settings.celery_queues == ["default"]
        assert settings.celery_queues[0] == "default"

    def test_cleanup_task_registered(self) -> None:
        assert celery_app.conf.task_routes == {"app.tasks.cleanup_tasks.*": {"queue": "default"}}
        schedule_tasks = {entry["task"] for entry in celery_app.conf.beat_schedule.values()}
        assert "app.tasks.cleanup_tasks.cleanup_tmp_objects" in schedule_tasks
        assert "app.tasks.cleanup_tasks.cleanup_tmp_objects" in celery_app.tasks
