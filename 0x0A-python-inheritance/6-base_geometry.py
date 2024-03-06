#!/usr/bin/python3
"""Module with minimal base class"""


class BaseGeometry:
    """A minimal base class representing geometry"""
    def area(self):
        """Work out area of a shape
        Raises: Exception - area() is not implemented
        """
        raise Exception("area() is not implemented")
