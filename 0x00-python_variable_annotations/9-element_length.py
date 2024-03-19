#!/usr/bin/env python3
"""stuff"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """split a string"""
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    print(element_length([["wee"], "will", "rock", "you"]))
