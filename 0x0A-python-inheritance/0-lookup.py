#!/usr/bin/python3
"""Module for function that lists attributes and methods
of a class or an object.
"""


def lookup(obj):
    """Get list of available attributes and methods
    of an object
    Args:
        obj: an object or class
    Returns: list of attributes and methods
    """
    if isinstance(obj, type):
        return obj().__dir__()
    return obj.__dir__()
