#!/usr/bin/python3
"""Define Square class"""


class Square:
    """Definition of a square
    Attributes:
        __size (int): size of the square sides.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of square
        Args:
            size (int): size of the square sides
            position (tuple): position of the square
        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) is tuple and len(position) == 2:
            if position[0] >= 0 and position[1] >= 0:
                self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculate area of the square
        Returns: the area (int)
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square
        Returns: None
        """
        for posY in range(self.__position[1]):
            print("")
        if self.__size == 0:
            print(" " * self.__position[0], end="")
            print("")
        else:
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
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

    @property
    def position(self):
        """Getter for the position attribute
        Returns: the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position
        Args:
            value (int): the tuple of value
        Returns: None
        """
        if type(value) is tuple and len(value) == 2:
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
