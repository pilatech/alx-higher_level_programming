#!/usr/bin/python3
"""Defines Square class"""


class Square:
    """Definition of a square with private instance attribute
    Attributes:
        __size (int): size of the square sides.
    """     
    def __init__(self, size):
        """Initialization of square
        Args:
            size (int): size of the square sides
        Return: None
        """
        self.__size = size
