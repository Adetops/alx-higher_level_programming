#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''function that computes the square value of all integers of a matrix

    Args:
        matrix: 2 dimensional array

    Return:
        A new matrix
            without modifying the original matrix
    '''
    new_matrix = []
    for i in range(len(matrix)):
        new = list(map(lambda x: x ** 2, matrix[i]))
        new_matrix.append(new)
    return (new_matrix)
