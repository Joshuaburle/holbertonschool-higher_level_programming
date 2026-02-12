#!/usr/bin/python3
"""
Module that defines a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]  # First element is always 1

        if triangle:
            last_row = triangle[-1]
            for j in range(1, i):
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)  # Last element is always 1

        triangle.append(row)

    return triangle
