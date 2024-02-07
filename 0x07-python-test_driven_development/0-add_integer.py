#!/usr/bin/python3
"""Implements addition of two integers.
"""


def add_integer(a, b=98):
    """Adds two integers.
    Args:
        a (int): first integer.
        b (int): second integer.
    Returns:
        (int) sum of a and b.
    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer
        if a or b are not integer or float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
