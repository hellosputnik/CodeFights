def spiralNumbers(n):
    square = [[0] * n for _ in xrange(n)]

    counter   = 1
    direction = 0
    x         = 0
    y         = 0
    X         = n
    Y         = n

    while counter <= n ** 2:
        if direction == 0:
            square[y][x] = counter
            x += 1
        if direction == 1:
            square[y][x] = counter
            y += 1
        if direction == 2:
            square[y][x] = counter
            x -= 1
        if direction == 3:
            square[y][x] = counter
            y -= 1

        counter += 1

        if direction == 0 and square[y][(x + 1) % n]:
            direction = 1
        if direction == 1 and square[(y + 1) % n][x]:
            direction = 2
        if direction == 2 and square[y][x - 1]:
            direction = 3
        if direction == 3 and square[y - 1][x]:
            direction = 0

    return square

