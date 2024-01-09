#!/usr/bin/python3
"""Library for"""


def pascal_triangle(n):
    """None"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(1)
            triangle.append(tmp)
    return triangle
