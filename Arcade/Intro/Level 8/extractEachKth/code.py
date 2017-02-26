def extractEachKth(inputArray, k):
    # Start at k - 1 because problem is not 0-based indexing.
    toDelete = range(k - 1, len(inputArray), k)

    offset = 0
    for indexToDelete in toDelete:
        del inputArray[indexToDelete - offset]
        offset += 1

    return inputArray

