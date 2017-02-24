def areSimilar(A, B):
    length      = len(A)
    differences = 0

    a, b = [], []
    for i in xrange(length):
        if A[i] != B[i]:
            a.append(A[i])
            b.append(B[i])
            differences += 1

    # If there are no differences, then similar.
    if differences == 0:
        return True

    # If there are exactly 2 differences AND the differences are the same,
    # then similar.
    if differences == 2 and sorted(a) == sorted(b):
        return True

    # Otherwise, not similar.
    return False

