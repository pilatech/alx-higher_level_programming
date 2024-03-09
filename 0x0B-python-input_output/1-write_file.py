#!/usr/bin/python3
"""Module for writing to file"""


def write_file(filename="", text=""):
    """Writes to file and counts how many characters writen
    Args:
        filename: name of the file to write to.
        text: the string to write
    Returns: number of characters writen
    """
    if filename:
        with open(filename, "w", encoding="utf-8") as f:
            return f.write(text)
