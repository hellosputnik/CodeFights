# The input is sorted so an optimized solution would start at the middle and
# work left or right, but I just want to finish this and move on.

def absoluteValuesSumMinimization(a):
    minimum = sum(map(lambda x: abs(x - a[0]), a))
    integer = a[0]

    for element in a[1:]:
        trial = 0
        for i in a:
            trial += abs(i - element)
            if trial > minimum:
                break
        if trial < minimum:
            minimum = trial
            integer = element

    return integer

# This is horrid solution is O(n ** 2). Do not copy!

