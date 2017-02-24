def arrayChange(inputArray):
    length = len(inputArray) - 1
    moves = 0

    for i in xrange(length):
        if inputArray[i] >= inputArray[i + 1]:
            increments = (inputArray[i] - inputArray[i + 1] + 1)
            moves += increments
            inputArray[i + 1] += increments

    return moves

