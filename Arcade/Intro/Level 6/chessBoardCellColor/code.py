def translate(cell):
    if cell[0] == "A":
        x = 0
    if cell[0] == "B":
        x = 1
    if cell[0] == "C":
        x = 2
    if cell[0] == "D":
        x = 3
    if cell[0] == "E":
        x = 4
    if cell[0] == "F":
        x = 5
    if cell[0] == "G":
        x = 6
    if cell[0] == "H":
        x = 7

    y = abs(int(cell[1]) - 8)

    return (x, y)

def chessBoardCellColor(cell1, cell2):
    rows    = 8
    columns = 8
    board   = []

    for row in xrange(rows):
        board.append([(column + row) % 2 for column in xrange(columns)])

    x1, y1 = translate(cell1)
    x2, y2 = translate(cell2)

    return board[y1][x1] == board[y2][x2]

