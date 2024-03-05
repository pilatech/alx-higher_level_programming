#!/usr/bin/python3
"""Module implementing instance comparison"""


def is_same_class(obj, a_class):
    """Check if an object is exactly instance of a class
    Args:
        obj: an object to test
        a_class: a class to test against
    Return: True or False
    """
    return type(obj) is a_class
