#!/usr/bin/python3
"""Module impleements Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Implements the Rectangle shape """
    def __init__(self, width, height):
        """initializ the Rectangle shape
         Args:
            width: the width of the rectangle
            height: the height of the rectangle
        Raises: validation Exceptions on failure
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__height = height
        self.__width = width

    def area(self):
        """Calculates area of the Rectangle
        Returns: area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Provides a printable version of the Rectangle
        Returns: string that reprents a Rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
