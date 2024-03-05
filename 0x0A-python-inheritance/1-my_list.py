#!/usr/bin/python3
"""Module for MyList that extends built-in list"""


class MyList(list):
    """Implementation of an augmented list"""
    def print_sorted(self):
        """Print list in sorted format.
        """
        temp = self[:]
        temp.sort()
        print(temp)
