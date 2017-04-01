def amendTheSentence(s):
    sentence = s[0].lower()

    for c in s[1:]:
        if c.isupper():
            sentence += " "
        sentence += c.lower()

    return sentence

