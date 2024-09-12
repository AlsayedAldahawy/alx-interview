#!/usr/bin/python3

'''
    Rotate a Matrix in place
'''


def rotate_2d_matrix(matrix):
    """
        Rotates a 2D matrix 90 degrees clockwise.

        Parameters:
        matrix (list of list of int): The 2D matrix to rotate.

        Returns:
        list of list of int: The rotated 2D matrix.
    """
    n = len(matrix[0])
    matr2 = [[matrix[i][j] for i in range(n - 1, -1, -1)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = matr2[i][j]
    return matrix
