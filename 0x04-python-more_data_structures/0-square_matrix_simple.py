def square_matrix_simple(matrix=[]):
    """
    new_matrix = [[num**2 for num in row] for row in matrix]
    return new_matrix
    """
    new_matrix = []
    for row in matrix:
        new_row = list(map(lambda x: x**2, row))
        new_matrix.append(new_row)
    return new_matrix
