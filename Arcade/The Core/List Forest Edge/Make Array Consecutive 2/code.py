def makeArrayConsecutive2(statues):
    statues = sorted(statues)
    length = len(statues)

    orders = 0
    for index in xrange(length - 1):
        if statues[index] + 1 != statues[index + 1]:
            orders += (statues[index + 1] - statues[index] - 1)

    return orders

