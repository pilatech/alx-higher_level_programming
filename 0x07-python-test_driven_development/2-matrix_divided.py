#!/usr/bin/python3
"""Implements division of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides matrix by a given dividend.
    Args:
        matrix: a list of list of integers or floats
        div: a number to divide each individual element in the matrix by.
    Returns:
        a new resultant matrix
    Raise:
        TypeError: on wrong type and format of either arguments
        ZeroDivisionError: when dividend is 0
    """
    new_matrix = []
    l_error = "matrix must be a matrix (list of lists) of integers/floats"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if type(matrix) is not list:
        raise TypeError(l_error)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(l_error)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(l_error)
            new_item = round(item / div, 2)
            new_row.append(new_item)
        new_matrix.append(new_row)
    return new_matrix
