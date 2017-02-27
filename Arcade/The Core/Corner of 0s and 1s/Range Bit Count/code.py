def rangeBitCount(a, b):
    return sum(map(lambda x: x.count("1"), map(bin, range(a, b + 1))))

