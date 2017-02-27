def circleOfNumbers(n, firstNumber):
    opposite = ((n / 2) + firstNumber)
    return opposite if firstNumber < (n / 2) else (opposite - n)

