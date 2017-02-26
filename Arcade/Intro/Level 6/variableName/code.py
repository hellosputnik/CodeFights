def variableName(name):
    if name[0] in "0123456789":
        return False

    for character in name:
        if not character.isalnum() and character != "_":
            return False

    return True

