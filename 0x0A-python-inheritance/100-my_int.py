#!/usr/bin/python3
"""Module implementing custom int type, MyInt"""


class MyInt(int):
    """Represents a custom int type"""
    def __eq__(self, other):
        """Implements custom equality. Inversion
        Args:
            other: the other integer to compare with
        Returns: True or False
        """
        return self is other

    def __ne__(self, other):
        """Implements custom inequality. Inversion
        Args:
            other: the other integer to compare with
        Returns: True or False
        """
        return self is not other
