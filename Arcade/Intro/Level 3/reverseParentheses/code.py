def reverse(s):
    left  = s.rfind("(")
    right = s.find(")")

    if left != -1 and right != -1:
        return s[:left] + s[right - 1:left:-1] + s[right + 1:]
    else:
        return s

def reverseParentheses(s):
    while "(" in s:
        s = reverse(s)
    return s

# This code is really bad. I'll fix it someday, but I'm so sick right now.

