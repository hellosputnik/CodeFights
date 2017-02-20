def allLongestStrings(inputArray):
    length  = len(inputArray[0])
    strings = [inputArray[0]]

    for string in inputArray[1:]:
        if len(string) == length:
            strings.append(string)
            continue

        if len(string) > length:
            length  = len(string)
            strings = [string]
            continue

        if len(string) < length:
            # Nothing to do. Skip.
            continue

    return strings

