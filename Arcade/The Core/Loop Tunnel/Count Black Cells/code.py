from fractions import gcd


def countBlackCells(n, m):
    return n + m + gcd(n, m) - 2

# Credit:
# http://math.stackexchange.com/questions/1121541/number-of-unit-squares-that-meet-a-given-diagonal-line-segment-in-more-than-one

