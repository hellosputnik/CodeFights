def sumOfTwo(a, b, v):
    # Convert a and b to sets for O(1) average case in-operations.
    a = set(a)
    b = set(b)

    # For each number in a, is the difference `in` b?
    for number in a:
        if v - number in b:
            return True

    # There were no pairs that added up to v.
    return False

