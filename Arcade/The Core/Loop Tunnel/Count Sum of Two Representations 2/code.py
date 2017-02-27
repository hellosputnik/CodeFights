def countSumOfTwoRepresentations2(n, l, r):
    count = 0

    for i in xrange(l, n / 2 + 1):
        if n - i <= r:
            count += 1

    return count

