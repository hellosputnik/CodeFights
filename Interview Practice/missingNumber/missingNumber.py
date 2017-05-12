def missingNumber(arr):
    n = max(arr)
    diff = ((n * (n + 1)) / 2) - sum(arr)

    if diff == 0:
        if 0 in arr:
            return n + 1
        else:
            return 0
    else:
        return diff

