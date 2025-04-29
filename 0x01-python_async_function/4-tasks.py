#!/usr/bin/env python3
"""Defines the task_wait_n function using task_wait_random"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns random wait n times and returns list of delays in asc order."""
    tasks: List[asyncio.Task]
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)

    return delays
