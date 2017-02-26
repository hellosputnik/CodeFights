from math import sqrt

def factor(x):
    return sorted(reduce(list.__iadd__, [[n, x / n] for n in range(1, int(sqrt(x)) + 1) if not (x % n)]))

def is_prime(x):
    return True if len(factor(x)) == 2 else False

def digitsProduct(product):
    # This should be 0 to be consistent with 1, 2, 3, ..., 9.
    if product == 0:
        return 10

    if product < 10:
        return product

    if is_prime(product):
        return -1

    factors = factor(product)
    result  = ""

    while product != 1:
        factors = filter(lambda x: x != 1 and x < 10, factors)
        if len(factors):
            f        = factors[-1]
            result  += str(f)
            product /= f
            factors  = factor(product)
        else:
            return -1

    return int("".join(sorted(result)))

