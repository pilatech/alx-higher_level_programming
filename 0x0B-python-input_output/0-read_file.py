#!/usr/bin/python3
"""Module for reading from file to stdout"""


def read_file(filename=""):
    """Reads file and print to stdout
    Args:
        filename: name of the file.
    """
    if filename:
        with open(filename, "r", encoding="utf-8") as f:
            for data in f:
                print(data, end="")
