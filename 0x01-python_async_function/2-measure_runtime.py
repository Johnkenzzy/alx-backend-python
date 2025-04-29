#!/usr/bin/env python3
"""Measure the total execution time for wait_n"""
import time
import asyncio
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time per wait_random call"""
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.perf_counter()

    total_time: float = end_time - start_time
    average_time: float = total_time / n
    return average_time
