def blur(image, x, y):
    total = 0

    total += image[x - 1][y - 1]
    total += image[x + 0][y - 1]
    total += image[x + 1][y - 1]

    total += image[x - 1][y + 0]
    total += image[x + 0][y + 0]
    total += image[x + 1][y + 0]


    total += image[x - 1][y + 1]
    total += image[x + 0][y + 1]
    total += image[x + 1][y + 1]

    return (total / 9)

def boxBlur(image):
    rows    = len(image)
    columns = len(image[0])

    answers = []
    for x in xrange(1, rows - 1):
        answer = []
        for y in xrange(1, columns - 1):
            answer.append(blur(image, x, y))
        answers.append(answer)

    return answers

