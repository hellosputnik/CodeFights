def difference(string1, string2):
    # This should never happen since the problem guarantees equal-length
    # strings, but it is good practice to be cautious.
    if len(string1) != len(string2):
        return -1

    length = len(string1)
    diff   = 0

    for index in xrange(length):
        if string1[index] != string2[index]:
            diff += 1

    return diff


def stringsRearrangement(inputArray):
    outputArray = [inputArray[0]]
    inputArray  = inputArray[1:]

    index = 0
    while index < len(inputArray):
        if difference(outputArray[0], inputArray[index]) == 1:
            outputArray.insert(0, inputArray[index])
            del inputArray[index]
            index = 0
            continue

        if difference(outputArray[-1], inputArray[index]) == 1:
            outputArray.append(inputArray[index])
            del inputArray[index]
            index = 0
            continue

        index += 1

    return True if not inputArray else False

