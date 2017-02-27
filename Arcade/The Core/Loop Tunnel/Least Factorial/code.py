from math import factorial


def leastFactorial(n):
    m = 0

    while factorial(m) < n:
        m += 1

    return factorial(m)

