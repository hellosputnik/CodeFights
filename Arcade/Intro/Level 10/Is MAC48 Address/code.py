def isMAC48Address(inputString):
    digits = inputString.split("-")

    if len(digits) != 6:
        return False

    for digit in digits:
        if len(digit) != 2:
            return False

        if digit[0] not in "0123456789ABCDEF":
            return False

        if digit[1] not in "0123456789ABCDEF":
            return False

    return True

