def translate(cell):
    x = 0

    if cell[0] == "a":
        x = 0
    if cell[0] == "b":
        x = 1
    if cell[0] == "c":
        x = 2
    if cell[0] == "d":
        x = 3
    if cell[0] == "e":
        x = 4
    if cell[0] == "f":
        x = 5
    if cell[0] == "g":
        x = 6
    if cell[0] == "h":
        x = 7

    y = abs(int(cell[1]) - 8)

    return (x, y)


def chessKnight(cell):
    moves = 0
    x, y  = translate(cell)

    if x - 2 >= 0:
        if y - 1 >= 0:
            moves += 1
        if y + 1 <= 7:
            moves += 1

    if x - 1 >= 0:
        if y - 2 >= 0:
            moves += 1
        if y + 2 <= 7:
            moves += 1

    if x + 1 <= 7:
        if y - 2 >= 0:
            moves += 1
        if y + 2 <= 7:
            moves += 1

    if x + 2 <= 7:
        if y - 1 >= 0:
            moves += 1
        if y + 1 <= 7:
            moves += 1

    return moves

