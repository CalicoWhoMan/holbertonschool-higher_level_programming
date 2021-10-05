#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    py_matrix = []
    for x in matrix:
        py_matrix.append(list(map(lambda row: row ** 2, x)))
    return py_matrix
