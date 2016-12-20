def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    i = 0
    total = 0
    while i < 10:
        if has_degit(n,i):
            total +=1
        i +=1
    return total


    "*** YOUR CODE HERE ***"
def has_degit(n,k):
    while n > 0:
        firstRightDigit , n = n % 10 , n //10
        if firstRightDigit == k:
            return True
    return False
