def addBorder(picture):
    length = len(picture[0]) + 2
    prefix = "*" * length
    suffix = prefix

    picture = ["*" + row + "*" for row in picture]

    return [prefix] + picture + [suffix]

