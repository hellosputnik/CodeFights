def sumDigit(integer):
    total = 0

    while integer:
        total   += integer % 10
        integer /= 10

    return total


def digitDegree(n):
    degree = 0

    while n >= 10:
        n = sumDigit(n)
        degree += 1

    return degree

