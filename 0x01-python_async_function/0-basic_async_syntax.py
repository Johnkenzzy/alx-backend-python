#!/usr/bin/env python3
"""Defines the wait_random async coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Awaits a random delay between 0 and max_delay and returns the delay"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
