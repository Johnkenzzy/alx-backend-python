#!/usr/bin/env python3
"""Defines the wait_random async coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Awaits a given time interval and return a random float value"""
    await asyncio.sleep(max_delay)
    return random.uniform(0, max_delay)
