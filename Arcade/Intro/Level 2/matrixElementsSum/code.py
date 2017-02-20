def matrixElementsSum(matrix):
    columns = len(matrix[0])
    costs   = 0
    rooms   = [1 for room in xrange(columns)]

    for row in matrix:
        for column in xrange(columns):
            cost = row[column]
            if cost != 0 and rooms[column] != 0:
                costs += cost
            else:
                rooms[column] = 0

    return costs

