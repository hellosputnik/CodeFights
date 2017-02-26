def alphabeticShift(inputString):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    result = ""
    for letter in inputString:
        result += alphabet[(alphabet.index(letter) + 1) % len(alphabet)]

    return result

