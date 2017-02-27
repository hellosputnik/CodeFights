def equalPairOfBits(n, m):
    return 2 ** (len(bin(n ^ m)[2:]) - ("0" + bin(n ^ m)[2:]).rfind("0"))

