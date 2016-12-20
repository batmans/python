def identity(k):
    return k

def square(k):
    return pow(k,2)


def product(n, term):
    """Return the product of the first n terms in a sequence.

    n    -- a positive integer
    term -- a function that takes one argument

    >>> product(3, identity) # 1 * 2 * 3
    6
    >>> product(5, identity) # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)   # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)   # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    """
    "*** YOUR CODE HERE ***"
    total , k = 1 , 1
    while k<=n:
        total, k = total*term(k), k+1
    return total

def factorial(n):
    return product(n,identity)

def product_square(n):
    return product(n,square)
