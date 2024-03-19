#!/usr/bin/env python3
"""
Defines a type-annotated function `make_multiplier` that takes
a float multiplier as argument and returns a function that
multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """create a closure with a multiplier"""
    return lambda n: n * multiplier


if __name__ == "__main__":
    multi = make_multiplier(2.0)
    print(multi(4.0))
