#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle:
    """Define a class that represents a rectangle
    Attributes:
        width (int): width of the rectangle.
        height (int): height of the reactangle.
        number_of_instances (cls attr): count instances.
        print_symbol(cls attr): set symbol to print rectangle with.
    """

    number_of_instances = 0
    print_symbol = "#"

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

        type(self).number_of_instances += 1

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

    def area(self):
        """Calculate the area of the rectangle.
        Returns: (int) area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.
        Returns: (int) the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Print/Draw the rectangle
        Returns: (str) the print version of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        print_str = ""
        for h in range(self.__height):
            for w in range(self.__width):
                if type(type(self).print_symbol) is str:
                    print_str += type(self).print_symbol
                else:
                    print_str += repr(type(self).print_symbol)
            if h < self.__height - 1:
                print_str += "\n"
        return print_str

    def __repr__(self):
        """Print parsable string of the rectangle object
        Returns: (str) a string that evaluates to object.
        """
        eval_str = "Rectangle(" + str(self.__width)
        eval_str += ", " + str(self.__height) + ")"
        return eval_str

    def __del__(self):
        """Leave a message on object deletion.
        Returns: None
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the bigger of the two rectangles
        based on area.
        Args:
            rect_1 (Rectangle): first rectangle.
            rect_2 (Rectangle): Second rectangle.
        Returns: (int) the larger of the two in area.
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_2.area() > rect_1.area()):
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Initialize a square.
        Args:
            size: the size of the side of the square.
        Returns: A square.
        """
        return cls(size, size)
