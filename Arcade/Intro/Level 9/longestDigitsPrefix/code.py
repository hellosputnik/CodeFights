def longestDigitsPrefix(inputString):
    for index, character in enumerate(inputString):
        if character not in "0123456789":
            return inputString[:index]

    # This line is executed when the entire string is composed of only digits.
    return inputString

