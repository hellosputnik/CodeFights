def isSumOfConsecutive2(n):
    if n == 1 or n == 2:
        return 0

    count = 0
    sequence = []

    # n / 2 + 2 because the upper bound is (n / 2) + 1, but range() excludes
    # the end.
    for i in xrange(n / 2 + 2):
        for index in xrange(len(sequence)):
            sequence[index] += i
        sequence.append(i)

        if n in sequence:
            count += 1

    return count

