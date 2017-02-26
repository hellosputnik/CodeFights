def messageFromBinaryCode(code):
    return "".join([chr(int(code[bit:bit + 8], 2)) for bit in xrange(0, len(code), 8)])

