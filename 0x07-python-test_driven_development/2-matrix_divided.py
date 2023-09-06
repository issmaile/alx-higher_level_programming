#!/usr/bin/python3
"""
The module defines a func that / all elems of a matrix
"""

def matrix_divided(matrix, div):
    """
    Divides all elems of a matrix by a num

    Args:
    matrix (list or lists): Input matrix of ints or floats
    div (int or float): The num to div by

    Returns:
    list or lists: A new matrix with elems divd by div, rounted to .00

    Raises:
    TypeError: If matrix is not a list of lists of ints or floats
    TypeError: If rows of the matrix have different sizes
    TypeError: If div is not a number (int or float)
    ZeroDevisionError: If div is 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")


    return [[round(num / div, 2) for num in row] for row in matrix]
