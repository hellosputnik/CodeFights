from re import sub


def sumUpNumbers(inputString):
    inputString = sub(r"(\W+|_)", " ", inputString)
    return sum(map(int, filter(lambda x: x.isdigit(), inputString.split())))

