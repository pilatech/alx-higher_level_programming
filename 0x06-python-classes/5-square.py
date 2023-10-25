#!/usr/bin/python3
"""Define Square class"""


class Square:
    """Definition of a square
    Attributes:
        __size (int): size of the square sides.
    """
    def __init__(self, size=0):
        """Initialization of square
        Args:
            size (int): size of the square sides
        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate area of the square
        Returns: the area (int)
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square
        Returns: None
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def size(self):
        """Getter for the size attribute
        Returns: the size (int)
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for the size attribute
        Args:
            size (int): size of the square.
        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
