#!/usr/bin/env python3
"""
Write a type-annotated function `to_kv` which takes a string `k`,
and a float | int `v` as argument and returns a tuple `(k, v^2)`.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """construct tuple of `k, v^2`"""
    return (k, v**2)
