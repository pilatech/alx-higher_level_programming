#!/usr/bin/python3
"""Module to check if an object's class is inherits from a given class"""


def inherits_from(obj, a_class):
    """Check if a class is in object's class heritage
    Args:
        obj: the object to check
        a_class: the class to check against
    Return:
        True or False
    """
    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
