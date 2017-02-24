def arrayMaximalAdjacentDifference(inputArray):
    length = len(inputArray)

    maxDifference = abs(inputArray[0] - inputArray[1])
    for i in xrange(1, length - 1):
        difference = abs(inputArray[i] - inputArray[i + 1])
        if difference > maxDifference:
            maxDifference = difference

    return maxDifference

