from re import sub


def longestWord(text):
    text = sub(r"(\W+|_)", " ", text)
    return max(text.split(), key=len)

