def add(a, b):
    result = 0

    for index in xrange(len(a)):
        result *= 10
        result += (int(a[index]) + int(b[index])) % 10

    return result


def additionWithoutCarrying(param1, param2):
    a = str(param1)
    b = str(param2)

    if len(a) > len(b):
        while len(a) > len(b):
            b = "0" + b

    if len(a) < len(b):
        while len(a) < len(b):
            a = "0" + a

    return add(a, b)

