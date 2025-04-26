#!/usr/bin/env python3
"""Defines the zoom_array function"""
from typing import List, Sequence, Any


def zoom_array(lst: Sequence[Any], factor: int = 2) -> List[Any]:
    """Return the appropiate collection type"""
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: List[int] = [12, 72, 91]

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)  # Fixed: pass an int, not a float
