def maxMultiple(divisor, bound):
    N = bound

    while N % divisor != 0:
        N -= 1

    return N

