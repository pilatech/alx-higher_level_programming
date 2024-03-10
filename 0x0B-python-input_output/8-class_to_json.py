#!/usr/bin/python3
"""class_to_json Module"""


def class_to_json(obj):
    """Turns object into a dictionary
    Args:
        obj: the object to turn
    Returns: a dictionary
    """
    return vars(obj)
