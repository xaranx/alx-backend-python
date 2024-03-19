#!/usr/bin/env python3
"""
Defines a type-annotated function `floor` that floors a floting point number.
"""


def floor(n: float) -> int:
    """floors the passed in float point number"""
    return int(n)


if __name__ == "__main__":
    vybs = floor(3.6)
    print(vybs)
