#!/usr/bin/python3
"""Module that converts object to JSON"""
import json


def to_json_string(my_obj):
    """Serializes an object (Converts to JSON)
    Args:
        my_obj: the object to serialize
    Returns: JSON string of the object.
    """
    return json.dumps(my_obj)
