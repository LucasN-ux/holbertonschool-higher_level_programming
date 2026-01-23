#!/usr/bin/python3
"""
Module add_integer
"""


def add_integer(a, b=98):
    """
    Adds two integers
    """

    for name, value in (("a", a), ("b", b)):
        if type(value) not in [int, float]:
            raise TypeError(f"{name} must be an integer")
        if isinstance(value, float) and (value != value or
           value in (float("inf"), float("-inf"))):
            raise TypeError(f"{name} must be an integer")

    return int(a) + int(b)
