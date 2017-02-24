from collections import Counter


def palindromeRearranging(inputString):
    frequencies = Counter(inputString)

    odds = 0
    for frequency in frequencies.values():
        if frequency % 2 != 0:
            odds += 1

    return True if odds <= 1 else False

