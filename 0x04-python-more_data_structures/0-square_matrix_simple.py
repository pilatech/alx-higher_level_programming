#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for arr in matrix:
        inner = [(x ** 2) for x in arr]
        matrix2.append(inner)
    return matrix2
