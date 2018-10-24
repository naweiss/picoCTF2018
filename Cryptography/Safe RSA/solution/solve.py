#!/usr/bin/python2

#https://stackoverflow.com/a/358134
def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    low = 10 ** (len(str(x)) / n)
    high = low * 10
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

# Don't use e=3 it's bad !!!
# Just compute cube root of c to find m
e = 3L
c = 2205316413931134031046440767620541984801091216351222789180582564557328762455422721368029531360076729972211412236072921577317264715424950823091382203435489460522094689149595951010342662368347987862878338851038892082799389023900415351164773L
m = find_invpow(c, e)

print(hex(m)[2:-1].decode('hex'))