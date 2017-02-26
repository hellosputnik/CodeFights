def fileNaming(names):
    seen = set()

    for index, name in enumerate(names):
        if name not in seen:
            seen.add(name)
        else:
            counter = 1
            newName = "{}({})".format(name, counter)
            while newName in seen:
                counter += 1
                newName  = "{}({})".format(name, counter)
            names[index] = newName
            seen.add(newName)

    return names

