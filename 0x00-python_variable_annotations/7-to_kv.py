#!/usr/bin/env python3
"""Defines the to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of mixed types"""
    return (k, float(v ** 2))
