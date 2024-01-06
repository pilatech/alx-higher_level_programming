#!/usr/bin/python3
"""Define the module for a Rectangle class"""


class Rectangle:
    """Define class that represents a Rectangle

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle

    """
    def __init__(self, width=0, height=0):
        """Initialize instance attributes
        Params:
            width (int): initial width of the rectangle
            height (int): initial height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """work with (ie get and set) value for width
        Params:
            value (int): new width to set

        If value is not integer, raise TypeError,
        if it's less than 0 raise ValueError
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
        """work with (ie get and set) value for height
        Params:
            value (int): new height to set

        If value is not integer, raise TypeError,
        if it's less than 0 raise ValueError
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
        """Return area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle
        if either height or width is 0 return 0
        """
        if (self.height == 0) or (self.width == 0):
            return 0
        else:
            return (self.height + self.width) * 2

    def __str__(self):
        """Return the printable version of the rectangle"""
        if (self.width == 0) or (self.height == 0):
            return ""
        else:
            grid = ""
            for h in range(self.height):
                for w in range(self.width):
                    grid += "#"
                if h != (self.height - 1):
                    grid += "\n"
            return grid
