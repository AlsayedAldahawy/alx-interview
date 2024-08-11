#!/usr/bin/python3

"""
Generates Pascal's triangle up to the specified number of rows.

Args:
    n (int): The number of rows in the Pascal's triangle.

Returns:
    list: A list of lists representing Pascal's triangle.

Example:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows.

    Args:
        n (int): Number of rows in the Pascal's triangle.

    Returns:
        list of lists: A list of lists representing Pascal's triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    tri = []

    for i in range(1, n + 1):
        row = [1] * i
        for j in range(i):
            if j == 0 or j == i - 1:
                continue
            else:
                row[j] = tri[-1][j] + tri[-1][j - 1]

        tri.append(row)
    return tri


'''
Explaining the algorithm of Pascal tringle:

Each element in every row, except for the first and last elements,\
    is the sum of the two adjacent elements in the previous row: the one at\
        the same position and the one immediately before it.

                 1
                1+1
              1+(2)+1      2 = 1+1
            1+(3)+(3)+1    3 = 1+(2), 3 = (2)+1
          1+(4)+(6)+(4)+1  4 = 1+(3), 6 = (3)+(3), 4 = (3)+1

'''
