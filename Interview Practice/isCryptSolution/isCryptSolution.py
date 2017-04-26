def isCryptSolution(crypt, solution):
    mappings    = dict(solution)
    cryptarithm = map(lambda x: "".join(map(lambda y: mappings[y], x)), crypt)

    if any(map(lambda x: x[0] == "0" and len(x) > 1, cryptarithm)):
        return False
    else:
        cryptarithm = map(int, cryptarithm)
        return cryptarithm[0] + cryptarithm[1] == cryptarithm[2]

