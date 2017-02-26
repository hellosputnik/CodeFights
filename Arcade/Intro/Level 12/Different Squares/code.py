def square(matrix, x, y):
    return (matrix[y][x], matrix[y][x + 1], matrix[y + 1][x], matrix[y + 1][x + 1])


def differentSquares(matrix):
    columns = len(matrix[0])
    rows    = len(matrix)
    seen    = set()

    for row in xrange(rows - 1):
        for column in xrange(columns - 1):
            seen.add(square(matrix, column, row))

    return len(seen)

