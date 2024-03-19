#!/usr/bin/env python3
"""Defines a type-annotated function `to_str` that takes a float `n`
as argument and returns the string representation of the float.
"""


def to_str(n: float) -> str:
    """stringifies a floating point number"""
    return str(n)


if __name__ == "__main__":
    vybs = to_str(3.14)
    print(vybs)
