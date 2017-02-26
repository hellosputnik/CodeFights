def isPalindrome(string):
    return string == string[::-1]

def buildPalindrome(st):
    length = len(st)

    reversedString = st[::-1]
    for index in xrange(1, length):
        string = st + reversedString[-index:]
        if isPalindrome(string):
            return string

    # This line should never be reached because the reversed string will be
    # appended in the worst case (which guarantees a palindrome).
    return False

