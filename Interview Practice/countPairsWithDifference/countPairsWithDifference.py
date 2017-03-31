import collections


def countPairsWithDifference(k, a):
    # The counter will hold the frequency of the numbers. The pairs is kept in
    # a set to avoid duplicates.
    counter = collections.defaultdict(int)
    pairs   = set()

    # For each number in a, add it to the counter and check if there is a pair.
    for number in a:
        # Calculate the difference `d`.
        d = number - k

        # Calculate the sum `s`.
        s = number + k

        # If the `d` has been seen, then it's a pair.
        if d in counter:
            pairs.add((d, number))

        # If the `s` has been seen, then it's a pair.
        if s in counter:
            pairs.add((number, s))

        # Add the number to the dictionary of seen numbers.
        counter[number] += 1

    # This variable will hold the result.
    result = 0

    # For each pair, multiply the occurrences to find the number of pairs
    # possible.
    for pair in pairs:
        result += (counter[pair[0]] * counter[pair[1]])

    # Return the result modulo by this constant (because the problem says so).
    return result % (10 ** 9 + 7)

