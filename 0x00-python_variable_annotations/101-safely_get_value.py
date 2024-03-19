#!/usr/bin/env python3
"""stuff"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """generics!!!"""
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == "__main__":
    print("Here's what the mappings should look like")

    annotations = safely_get_value.__annotations__
    for k, v in annotations.items():
        print(("{}: {}".format(k, v)))
