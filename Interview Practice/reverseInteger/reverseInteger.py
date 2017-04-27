def reverseInteger(x):
    if x >= 0:
        return int(str(x)[::-1])
    else:
        return int(str(x)[:0:-1]) * -1

