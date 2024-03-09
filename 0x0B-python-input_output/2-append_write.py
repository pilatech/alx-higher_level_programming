#!/usr/bin/python3
"""Module for appending to file"""


def append_write(filename="", text=""):
    """Appends to file and counts how many characters writen
    Args:
        filename: name of the file to write to.
        text: the string to write
    Returns: number of characters writen
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            return f.write(text)
