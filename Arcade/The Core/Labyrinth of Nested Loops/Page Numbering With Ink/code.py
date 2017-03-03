def pagesNumberingWithInk(current, numberOfDigits):
    if len(str(current)) > numberOfDigits:
        return (current - 1)

    return pagesNumberingWithInk(current + 1, numberOfDigits - len(str(current)))

