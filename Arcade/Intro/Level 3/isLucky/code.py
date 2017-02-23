def isLucky(n):
    length = len(str(n))
    if length % 2 != 0:
        return False

    firstHalf  = sum([int(c) for c in str(n)[:length / 2]])
    secondHalf = sum([int(c) for c in str(n)[length / 2:]])

    return firstHalf == secondHalf

