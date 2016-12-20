def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    n = 1
    while True:
        if n % a == 0 and n % b == 0 :
            return n
        n +=1
