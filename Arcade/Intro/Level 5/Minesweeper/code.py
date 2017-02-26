def add(field, mine):
    x, y = mine

    X = len(field[0])
    Y = len(field)

    if x - 1 != -1 and y - 1 != -1:
        field[y - 1][x - 1] += 1
    if y - 1 != -1:
        field[y - 1][x + 0] += 1
    if x + 1 != X and y - 1 != -1:
        field[y - 1][x + 1] += 1

    if x - 1 != -1 :
        field[y + 0][x - 1] += 1
    if x + 1 != X:
        field[y + 0][x + 1] += 1

    if x - 1 != -1 and y + 1 != Y:
        field[y + 1][x - 1] += 1
    if y + 1 != Y:
        field[y + 1][x + 0] += 1
    if x + 1 != X and y + 1 != Y:
        field[y + 1][x + 1] += 1


def minesweeper(matrix):
    rows    = len(matrix)
    columns = len(matrix[0])
    field   = [[0] * columns for row in xrange(rows)]

    for row in xrange(rows):
        for column in xrange(columns):
            if matrix[row][column]:
                add(field, (column, row))

    return field

