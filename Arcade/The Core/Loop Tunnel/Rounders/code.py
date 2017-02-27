def rounders(value):
    length = len(str(value))

    for digit in xrange(length):
        value = round(value, -digit)

    return value

