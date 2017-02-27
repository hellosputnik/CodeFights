def appleBoxes(k):
    boxes = [i ** 2 for i in xrange(1, k + 1)]
    return sum(boxes[1::2]) - sum(boxes[0::2])

