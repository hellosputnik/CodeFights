def phoneCall(min1, min2_10, min11, s):
    minutes = 0

    if min1 > s:
        return 0

    s -= min1
    minutes = 1

    s2_10 = s / min2_10

    if s2_10 < 9:
        minutes += s2_10
        return minutes

    s2_10 = 9
    s -= (min2_10 * s2_10)
    minutes += (s2_10)

    if s > min11:
        minutes += (s / min11)

    return minutes

