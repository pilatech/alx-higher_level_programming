#!/usr/bin/python3
"""Module that loads data from a file and converts to JSON"""
import json


def load_from_json_file(filename):
    """Loads data from a file and converts it to json
    Args:
        filename: the file to load from
    Returns: a python object
    """
    if filename:
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()
            return json.loads(data)
