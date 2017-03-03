from math import sqrt

def factor(x):
    return sorted(reduce(list.__iadd__, [[n, x / n] for n in range(1, int(sqrt(x)) + 1) if not (x % n)]))

def isPower(n):
    if n == 1:
        return True

    for f in factor(n)[1:]:
        trial = f
        while trial < n:
            trial *= f
            if trial == n:
                return True

    return False

