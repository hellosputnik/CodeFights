def sudoku(grid):
    for row in grid:
        if len(set(row)) != 9:
            return False

    for c in xrange(9):
        column = set()
        for row in grid:
            column.add(row[c])
        if len(column) != 9:
            return False

    for y in xrange(0, 9, 3):
        for x in xrange(0, 9, 3):
            matrix = set()

            matrix.add(grid[y + 0][x + 0])
            matrix.add(grid[y + 0][x + 1])
            matrix.add(grid[y + 0][x + 2])
            matrix.add(grid[y + 1][x + 0])
            matrix.add(grid[y + 1][x + 1])
            matrix.add(grid[y + 1][x + 2])
            matrix.add(grid[y + 2][x + 0])
            matrix.add(grid[y + 2][x + 1])
            matrix.add(grid[y + 2][x + 2])

            if len(matrix) != 9:
                return False

    return True

