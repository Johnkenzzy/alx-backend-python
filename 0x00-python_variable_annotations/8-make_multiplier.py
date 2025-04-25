#!/usr/bin/env python3
"""Defines the make_muliplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a multiplier function"""
    def multiplier_function(n: float) -> float:
        """Multiplies two float numbers"""
        return n * multiplier
    return multiplier_function
