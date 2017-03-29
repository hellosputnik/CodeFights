def sumInRange(nums, queries):
    result = []

    i = 1
    while i < len(nums):
        nums[i] += nums[(i - 1)]
        i += 1

    for query in queries:
        if query[0] == 0:
            result.append(nums[query[1]])
        else:
            result.append(nums[query[1]] - nums[(query[0] - 1)])

    return sum(result) % (10 ** 9 + 7)

