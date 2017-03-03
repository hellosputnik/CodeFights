def construct(a):
    return sum(map(lambda x: int(x) ** 2, str(a)[::]))


def squareDigitsSequence(a0):
    length = 1

    seen = set()

    while a0 not in seen:
        seen.add(a0)
        a0 = construct(a0)
        length += 1

    return length

