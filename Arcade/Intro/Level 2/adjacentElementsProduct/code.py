def adjacentElementsProduct(inputArray):
    length         = len(inputArray)
    largestProduct = inputArray[0] * inputArray[1]

    for index in xrange(1, length - 1):
        product = inputArray[index] * inputArray[index + 1]

        if product > largestProduct:
            largestProduct = product

    return largestProduct

