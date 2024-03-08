#!/usr/bin/python3
"""Module for reading from file to stdout"""


def read_file(filename=""):
    """Reads file and print to stdout
    Args:
        filename: name of the file.
    """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data)
