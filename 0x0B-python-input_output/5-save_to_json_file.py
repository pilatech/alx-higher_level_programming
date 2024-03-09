#!/usr/bin/python3
"""Module that converts object to JSON and save to file"""
import json


def save_to_json_file(my_obj, filename):
    """Serializes an object and saves the string to file
    Args:
        my_obj: the object to serialize
        filename: the file to save to
    """
    if filename:
        with open(filename, "w", encoding="utf-8") as f:
            data = json.dumps(my_obj)
            f.write(data)
