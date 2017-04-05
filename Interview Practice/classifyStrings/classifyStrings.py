VOWELS = ['a', 'e', 'i', 'o', 'u']


def bad(s):
    counter = 0

    previous = 'v'
    for i, c in enumerate(s):
        if c in VOWELS:
            if previous == 'c':
                counter = 0
            counter += 1
            previous = 'v'
        else:
            if previous == 'v':
                counter = 0
            counter -= 1
            previous = 'c'
        if counter == 3:
            return True
        if counter == -5:
            return True

    return False


def generate(s):
    queue   = []
    results = []

    queue.append(s)
    while queue:
        string = queue.pop(0)
        index = string.find("?")

        if index != -1:
            queue.append(string.replace("?", "a", 1))
            queue.append(string.replace("?", "b", 1))
        else:
            results.append(string)

    return results


def classifyStrings(s):

    results =  map(bad, generate(s))

    if True in results:
        if False in results:
            return "mixed"
        else:
            return "bad"
    else:
        return "good"

    return "1337 h4x0r"

