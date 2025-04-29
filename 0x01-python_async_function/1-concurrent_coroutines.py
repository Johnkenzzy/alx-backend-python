#!/usr/bin/env python3
"""Defines the wait_n async coroutine"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return list of delays in asc order"""
    tasks: List[asyncio.Task]
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
