def magicalWell(a, b, n):

    return a * b + magicalWell(a + 1, b + 1, n - 1) if n else 0

