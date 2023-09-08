#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if j < len(row) - 1:
                print("{}".format(element), end=' ')
            else:
                print("{}".format(element), end='')
        print()
