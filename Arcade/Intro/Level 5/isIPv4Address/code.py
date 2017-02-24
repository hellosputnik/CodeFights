def isIPv4Address(inputString):
    bytes = inputString.split(".")

    if len(bytes) != 4:
        return False

    for byte in bytes:
        try:
            number = int(byte)
            if number < 0 or number > 255:
                return False
        except:
            return False

    return True

