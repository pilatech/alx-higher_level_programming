#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes Rectangle attributes
        Args:
            width (int): the longer side of the rectangle.
            height (int): the shorter side of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves and Sets value for width

        Args:
            value (int): the value for width.
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        Returns: the value of width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves and Sets value for height

        Args:
            value (int): the value for height.
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        Returns: the value of width.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the Rectangle area

        Returns:
            int: area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the Perimeter of the Rectangle

        Returns:
            int: the rectangle perimeter or 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
