#!/usr/bin/env python3
"""
Defines a type-annotated function `add` that takes a float `a`
and a float `b` as arguments and returns the addition of both args.
"""


def add(a: float, b: float) -> float:
    """add two floats and returns the result."""
    return a + b


if __name__ == "__main__":
    vybs = add(2.1, 4.5)
    print(vybs)
