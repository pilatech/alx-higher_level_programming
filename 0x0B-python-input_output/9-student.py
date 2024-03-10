#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """Defines a Student object"""

    def __init__(self, first_name, last_name, age):
        """Initialize the Student object
        Args:
            first_name: the student's first name
            last_name: the student's last name
            age: the student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Turns instances of the student to JSON
        Return: A serializable object (dict)
        """
        return vars(self)
