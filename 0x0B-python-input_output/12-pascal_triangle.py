#!/usr/bin/python3
"""Pascal Triangle module"""


def pascal_triangle(n):
    """Represents Pascal triangle with list of lists
    Args:
        n: height of the triangle
    """
    pascal = []
    temp = []
    if n <= 0:
        return [] 
    for i in range(5):
        pascal.append(2**i)
    print(pascal)
