from collections import Counter


def isBeautifulString(inputString):
    counter = Counter(inputString)

    alpha = "abcdefghijklmnopqrstuvwxyz"

    for index in xrange(len(alpha) - 1):
        if counter[alpha[index]] < counter[alpha[index + 1]]:
            return False

    return True

