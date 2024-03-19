#!/usr/bin/env python3
"""
Defines a type-annotated function `concat` that takes a string `str1`
and a string `str2` as arguments and returns a concatenated string.
"""


def concat(str1: str, str2: str) -> str:
    """concatenates two strings and returns the result."""
    return str1 + str2


if __name__ == "__main__":
    vybs = concat("hello", "world")
    print(vybs)
