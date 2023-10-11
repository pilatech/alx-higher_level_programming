#!/usr/bin/python3
def pow(a, b):
    if (b == 0):
        return 1

    product = 1
    i = 0
    if (b < 0):
        while i < -b:
            product *= (1 / a)
            i += 1
    else:
        while i < b:
            product *= a
            i += 1
    return product
