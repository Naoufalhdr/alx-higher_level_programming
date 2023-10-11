#!/usr/bin/python3
"""Define a Pascals triangle function"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle as a list of lists of integers for a given
    value of n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for row in range(n):
        current_row = [1]
        if row > 0:
            previous_row = triangle[row - 1]
            for i in range(1, row):
                current_value = previous_row[i - 1] + previous_row[i]
                current_row.append(current_value)
            current_row.append(1)
        triangle.append(current_row)
    return triangle
