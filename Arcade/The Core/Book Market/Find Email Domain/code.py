from re import search


# This isn't exactly a thorough parse, but it suffices for this problem since
# we are guaranteed a valid e-mail address.
def findEmailDomain(address):
    return search(".+@([^@]+)", address).group(1)

