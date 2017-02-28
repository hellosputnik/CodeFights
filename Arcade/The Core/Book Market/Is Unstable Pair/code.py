def isUnstablePair(filename1, filename2):
    return sorted([filename1, filename2]) != \
           sorted([filename1, filename2], key=unicode.lower)

