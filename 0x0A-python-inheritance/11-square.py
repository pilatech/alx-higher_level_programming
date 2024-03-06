#!/usr/bin/python3
"""Module impleements Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Implements the Square shape """
    def __init__(self, size):
        """initializ the Rectangle shape
         Args:
            size: the size of the square sides
        Raises: validation Exceptions on failure
        """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """Calculate the area of the Square
        Returns: area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """Creates the printable version of the Square
        Returns: the printable string
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
