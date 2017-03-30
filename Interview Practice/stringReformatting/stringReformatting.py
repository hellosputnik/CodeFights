def stringReformatting(s, k):
    # Allocate a list to hold the characters of the string.
    characters = []

    # Extract the characters in string `s` that are not "-".
    for c in s:
        if c != "-":
            characters.append(c)

    # Handle the case when k = 1.
    if k == 1:
        return "-".join(characters)

    # Calculate the variables needed to insert the dashes.
    length      = len(characters)
    firstDash   = length % k
    totalDashes = length / k - 1

    # If there are no dashes to insert, return the characters as a string.
    if totalDashes == -1:
        return "".join(characters)

    # Handle the initial dash, which may be contain less than k-characters.
    i = 0
    if firstDash != 0:
        characters.insert(firstDash, "-")
        i = firstDash + 1

    # Insert the dashes into the list of characters.
    counter = 0
    while counter < totalDashes:
        i += k
        characters.insert(i, "-")
        i += 1
        counter += 1

    # Return the string with the dashes inserted.
    return "".join(characters)

