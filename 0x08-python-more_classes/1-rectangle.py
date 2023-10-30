#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle:
    """Define a class that represents a rectangle
    Attributes:
        width (int): width of the rectangle.
        height (int): height of the reactangle.
    """
    def __init__(self, width=0, height=0):
        """Initialize a rectangle.
        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        Returns: None
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def width(self):
        """Get the width of the rectangle.
        Returns: (int) width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        Args:
            value (int): the value to set to.
        Returns: None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.
        Returns: (int) height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        Args:
            value (int): the value to set to.
        Returns: None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
