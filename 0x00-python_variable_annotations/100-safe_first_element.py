#!/usr/bin/env python3
"""Defines the safe_first_element function"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element or None if not"""
    if lst:
        return lst[0]
    else:
        return None
