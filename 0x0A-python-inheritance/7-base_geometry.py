#!/usr/bin/python3
"""Module with minimal base class"""


class BaseGeometry:
    """A minimal base class representing geometry"""
    def area(self):
        """Work out area of a shape
        Raises: Exception - area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer value
        Args:
            name: attribute name
            value: the value of the attribute
        Raises: TypeError if value is not an integer
                ValueError is value is less than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
