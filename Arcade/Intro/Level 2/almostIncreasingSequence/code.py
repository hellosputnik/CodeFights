def almostIncreasingSequence(sequence):
    length         = len(sequence)
    largestInteger = sequence[0]
    erases         = 0

    if length == 2:
        return True

    if largestInteger == max(sequence):
        for integer in sequence[1:]:
            if integer > largestInteger:
                return False

    else:
        for integer in sequence[1:]:
            if integer <= largestInteger:
                erases += 1
                if erases > 1:
                    return False
            else:
                largestInteger = integer

    return True

