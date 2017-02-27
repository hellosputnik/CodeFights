def replaceMiddle(arr):
    length = len(arr)
    middle = length / 2

    if length % 2 == 0:
        return arr[:middle - 1] + \
               [arr[middle - 1] + arr[middle]] + \
               arr[middle + 1:]
    else:
        return arr

