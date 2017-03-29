def singleNumber(nums):
    return reduce(lambda x, y: x ^ y, nums)

