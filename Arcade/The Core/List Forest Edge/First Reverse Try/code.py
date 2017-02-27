def firstReverseTry(arr):
    if not arr:
        return []

    if len(arr) == 1:
        return arr

    arr[0]  ^= arr[-1]
    arr[-1] ^= arr[0]
    arr[0]  ^= arr[-1]

    return arr

