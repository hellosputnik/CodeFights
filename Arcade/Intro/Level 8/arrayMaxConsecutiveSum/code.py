from collections import deque


def arrayMaxConsecutiveSum(inputArray, k):
    slice = deque(inputArray[0:k])
    total = sum(slice)

    maximum = total
    for element in inputArray[k:]:
        # Shift the slice/window.
        total -= slice.popleft()
        total += element
        slice.append(element)

        # Record the new slice/window if it's the larger than the previous
        # largest.
        if total > maximum:
            maximum = total

    return maximum

