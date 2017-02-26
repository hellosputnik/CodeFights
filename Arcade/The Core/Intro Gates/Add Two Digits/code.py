def addTwoDigits(n):
    return reduce(lambda x, y: int(x) + int(y), str(n))

