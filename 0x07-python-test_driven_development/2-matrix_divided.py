#!/usr/bin/python3


def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None or len(matrix) == 0:
        raise TypeError(message)
    new_matrix = []
    lenght = len(matrix[0])
    for row in matrix:
        if len(row) != lenght:
            raise TypeError("Each row of the matrix must have the same size")
        if (not row or
                not isinstance(row, list) or
                not all(isinstance(digit, (int, float)) for digit in row)):
            raise TypeError(message)

        new_row = [round(digit / div, 2) for digit in row]
        new_matrix.append(new_row)

    return (new_matrix)
