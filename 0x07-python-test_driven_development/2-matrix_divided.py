#!/usr/bin/python3
""" Defines a matrix division function. """

def matrix_divided(matrix, div):
    """ Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats
        div (int / float): The divisor.
    Raises:
        TypeError: If matrix contains non-numbers, or rows of different sizes.
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix containing the result of the division.
    """

    err_mess = "matrix must be a matrix (list of lists) of integers/floats"
    
    for elem in [num for row in matrix for num in row]:
        if (not isinstance(matrix, list) or (matrix == []) or
                (not all(isinstance(row, list) for row in matrix) or
                (not all((isinstance(ele, int) or isinstance(ele, float)))):
            raise TypeError(err_mess)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
