#!/usr/bin/python3
"""Module that converts string to Python object"""
import json


def from_json_string(my_str):
    """Deserializes an object
    Args:
        my_str: the string to deserialize
    Returns: a python object.
    """
    return json.loads(my_str)
