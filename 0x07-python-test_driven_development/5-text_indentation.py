#!/usr/bin/python3
"""Implements indentation of text by two new lines
"""


def text_indentation(text):
    """Indents text by two new lines
    Args:
        text: the text to indent.
    Raises:
        TypeError: if the text is not a string.
    """
    if type(text) is not (str):
        raise TypeError("text must be a string")
    for letter in text:
        if letter == "." or letter == "?" or letter == ":":
            print(letter)
            print("")
        else:
            print(letter, end="")
