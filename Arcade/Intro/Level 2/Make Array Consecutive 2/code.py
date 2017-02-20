def makeArrayConsecutive2(statues):
    length        = len(statues)
    sortedStatues = sorted(statues)
    orders        = 0

    for index in xrange(length - 1):
        if statues[index] + 1 != statues[index + 1]:
            orders += statues[index + 1] - statues[index] - 1

    return orders

