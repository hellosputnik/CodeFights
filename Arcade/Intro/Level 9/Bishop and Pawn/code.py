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


def bishopAndPawn(bishop, pawn):
    bx, by = translate(bishop)
    px, py = translate(pawn)

    return abs(bx - px) == abs(by - py)

