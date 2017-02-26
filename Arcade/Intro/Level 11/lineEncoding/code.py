def lineEncoding(s):
    count     = 1
    character = s[0]
    result    = ""

    for c in s[1:]:
        if c == character:
            count += 1
        else:
            if count == 1:
                result += character
                character = c
            else:
                result += str(count) + character
                count  = 1
                character = c

    if count == 1:
        result += character
    else:
        result += str(count) + character

    return result

