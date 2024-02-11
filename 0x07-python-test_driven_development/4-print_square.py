#!/usr/bin/python3
"""Implements square print
"""


def print_square(size):
    """Prints a square using # symbols
    Args:
        size: square width/height
    Raises:
        TypeError: for wrong type
        ValueError: if size is less than 0.
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for w in range(size):
        print("#" * size)
