#!/usr/bin/python3
"""
A matrix module that must be
a list os lists
Each row and column must the same size
same size of in and float
"""


def matrix_divided(matrix, div):
    """Defined function for matrix"""
    ex_msg = "matrix must be a matrix (list of lists) of integers/floats"
    size_msg = "Each row of the matrix must have the same size"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(ex_msg)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(ex_msg)
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError(ex_msg)
    lent = len(matrix[0])
    for row in matrix:
        if lent != len(row):
            raise TypeError(size_msg)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]


