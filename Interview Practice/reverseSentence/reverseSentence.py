import re

def reverseSentence(sentence):
    return "".join(reversed(re.split(r"(\s+)", sentence)))

