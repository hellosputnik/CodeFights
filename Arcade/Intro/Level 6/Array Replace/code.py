def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for index, element in enumerate(inputArray):
        if element == elemToReplace:
            inputArray[index] = substitutionElem

    return inputArray

