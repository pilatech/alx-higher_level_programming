#!/usr/bin/python3
"""Module for a function that tries to add attribute to an object"""


def add_attribute(obj, name, value):
    """Tries to add attribute named name and value to an object
    Args:
        obj: an object to add to.
        name: an attribute to add
        value: value of the attribute
    Raises: TypeError if you can't add to the object.
    """
    if (isinstance(obj, MutableSequence) or 
    isinstance(obj, MutableSet) or 
    isinstance(obj, MutableMapping)):
        obj[name] = value
    else:
        raise TypeError("can't add new attribute")

