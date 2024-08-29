#!/usr/bin/python3
""" calculates the perimeter of an island """


def calc(grid, i, j, direction):
    """ calculates the primeter of the current square `v` vertically
    or `h` horizontally """
    out = 0
    h = [j - 1, j + 1]
    v = [i - 1, i + 1]
    col = len(grid) - 1
    row = len(grid[i]) - 1

    if direction == "h":
        for d in h:
            if (d > row or d < 0) or grid[i][d] == 0:
                out += 1
    elif direction == "v":
        for d in v:
            if (d > col or d < 0) or grid[d][j] == 0:
                out += 1

    return out


def island_perimeter(grid):
    """ calculates the perimeter of an island """
    peri = 0

    if not grid or len(grid) > 100 or len(grid[0]) > 100:
        return

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j]):
                peri += calc(grid, i, j, "h")
                peri += calc(grid, i, j, "v")

    return peri
