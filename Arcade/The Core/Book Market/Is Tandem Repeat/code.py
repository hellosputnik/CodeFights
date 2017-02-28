def isTandemRepeat(inputString):
    length = len(inputString)
    return inputString[:length / 2] == inputString[length / 2:]

