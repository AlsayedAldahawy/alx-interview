#!/usr/bin/python3

def pascal_triangle(n):

    tri = []

    for i in range(1, n + 1):
        row = [1] * i
        for j in range(i):
            if j == 0 or j == i - 1:
                continue
            else:
                row[j] = tri[-1][j] + tri[-1][j - 1]

        tri.append(row)
    return (tri)
