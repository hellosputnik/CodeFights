def arrayPacking(a):
    return reduce(lambda x, y: (x << 8) | y, a[::-1])

