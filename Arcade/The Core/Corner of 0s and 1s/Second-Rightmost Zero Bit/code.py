def secondRightmostZeroBit(n):
    return 2 ** (len(bin(n)[2:]) - bin(n)[2:].rfind("0", 0, bin(n)[2:].rfind("0")) - 1)

