#!/usr/bin/env python3
"""Collects 10 random numbers from an async generator"""
from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Collects and returns 10 random numbers from async_generator"""
    return [i async for i in async_generator()]
