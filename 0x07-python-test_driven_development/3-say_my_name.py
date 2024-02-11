#!/usr/bin/python3
"""Implements a function that prints full name
"""


def say_my_name(first_name, last_name=""):
    """Prints out full name
    Args:
        first_name: first name string.
        last_name: optional last name string.
    Raises:
        TypeError: if wrong first name or last name type is given.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
