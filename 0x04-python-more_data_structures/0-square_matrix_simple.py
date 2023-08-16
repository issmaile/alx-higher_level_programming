#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for col in range(len(new_matrix)):
        for i in range(len(new_matrix[col])):
            new_matrix[col][i] **= 2
    return new_matrix
