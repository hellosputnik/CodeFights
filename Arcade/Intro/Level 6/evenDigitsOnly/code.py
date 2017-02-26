def evenDigitsOnly(n):
    while n != 0:
        # Get the digit.
        digit = n % 10

        # If the digit is odd, then exit and return False.
        if digit == 1 or \
           digit == 3 or \
           digit == 5 or \
           digit == 7 or \
           digit == 9:
            return False

        # Move onto the next digit.
        n /= 10

    # This function will only return True if no odd digits were found.
    return True

