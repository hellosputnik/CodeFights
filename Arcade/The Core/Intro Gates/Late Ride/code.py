def digitSum(n):
    return int(reduce(lambda x, y: int(x) + int(y), str(n)))


def lateRide(n):
    return digitSum(n / 60) + digitSum(n % 60)

