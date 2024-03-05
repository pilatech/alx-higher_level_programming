#!/usr/bin/python3
"""Module to check if a class exists in object's inheritance chain"""


def is_kind_of_class(obj, a_class):
    """Check if object is of a class kind
    Args:
        obj: the object to check
        a_class: the class to check against
    Return:
        True or False
    """
    return isinstance(obj, a_class)
