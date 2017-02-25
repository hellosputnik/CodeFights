def avoidObstacles(inputArray):
    maxJump = max(inputArray) + 1

    for jump in xrange(2, maxJump):
        test = jump
        while test < maxJump:
            if test in inputArray:
                break
            test += jump
        if test >= maxJump:
            return jump

    return maxJump

