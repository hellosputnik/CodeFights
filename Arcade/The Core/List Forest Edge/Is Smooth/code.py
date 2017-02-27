def isSmooth(arr):
    length = len(arr)
    middle = length / 2

    if length % 2 == 0:
        return arr[0] == arr[-1] and \
               arr[0] == arr[middle] + arr[middle - 1]
    else:
        return arr[0] == arr[-1] and \
               arr[0] == arr[middle]

