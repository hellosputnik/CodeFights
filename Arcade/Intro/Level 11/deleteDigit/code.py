def deleteDigit(n):
    number    = str(n)
    length    = len(number)
    maxNumber = int(number[1:])

    for index in xrange(1, length):
        trial = int(number[:index] + number[index + 1:])
        if trial > maxNumber:
            maxNumber = trial

    return maxNumber

