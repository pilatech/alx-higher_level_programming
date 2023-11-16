#!/usr/bin/python3
"""
Create a function to add two integers
"""


def add_integer(a, b=98):
    """Add two integers
    Args:
        a (int): first number to add.
        b (int): second number to add.
    Returns: (int) sum of a and b.
    """
    if type(a) is not int and type(a) is not float:
        print("a is not int or float => ", a)
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        print("b is not int or float => ", b)
        raise TypeError('b must be an integer')
    return int(a) + int(b)
