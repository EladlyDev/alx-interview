#!/usr/bin/python3
"""pascal's triangle function"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to a given number of rows.

    Args:
        n (int): The number of rows to generate in the triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    out = [[1]]
    n -= 1

    for i in range(0, n):
        if len(out) == 1:
            out.append([1, 1])
            continue
        row = [1]
        for j in range(1, len(out[i])):
            val = out[i][j] + out[i][j-1]
            row.append(val)
        row.append(1)
        out.append(row)

    return out
