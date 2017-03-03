from math import sqrt

def factor(x):
    return sorted(reduce(list.__iadd__, [[n, x / n] for n in range(1, int(sqrt(x)) + 1) if not (x % n)]))


def d(x):
    return len(set(factor(x)))

def weakNumbers(n):
    count   = 0
    weakest = 0

    table = []
    for i in xrange(1, n + 1):
        divisors = d(i)
        weakness = len(filter(lambda x: x > divisors, table))
        if weakness == weakest:
            count += 1
        if weakness > weakest:
            count   = 1
            weakest = weakness
        table.append(divisors)

    return [weakest, count]

