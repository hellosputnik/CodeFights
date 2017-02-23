from collections import deque


def sortByHeight(s):
    heights = deque()
    length  = len(s)

    for value in s:
        if value != -1:
            heights.append(value)

    heights = deque(sorted(heights))

    for index in xrange(length):
        if s[index] == -1:
            continue
        else:
            s[index] = heights.popleft()

    return s

