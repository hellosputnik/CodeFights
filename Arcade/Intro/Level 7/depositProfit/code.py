from math import ceil, log


# A = P * (1 + (r / n)) ^ (n * t)
#
# A     The future value of the investment
# P     The principal investment amount (i.e. initial deposit)
# r     The annual interest rate as a decimal
# n     The number of times that the interest is compounded per year
# t     The number of years the money is invested
#
# Solved for t.
#
# t = log(A / P) / log(r + 1)
def depositProfit(deposit, rate, threshold):
    return ceil(log(threshold / float(deposit)) / log(rate / 100.0 + 1))

