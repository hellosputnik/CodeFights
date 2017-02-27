def lineUp(commands):
    count     = 0
    direction = 0

    for command in commands:
        if command == "A":
            if direction ==  1:
                direction = -1
            if direction == -1:
                direction =  1

        if command == "L":
            if direction == -1:
                direction = 0
            else:
                direction -= 1

        if command == "R":
            if direction == 1:
                direction = 0
            else:
                direction += 1

        if direction == 0:
            count += 1

    return count

