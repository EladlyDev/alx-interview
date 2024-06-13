#!/usr/bin/python3
""" The minimum nomper of operations """


def factors(n):
    """ returns the factors of a number """
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                yield i
                break


def minOperations(n):
    """ returns the menimum number of operations to achieve H of length n """
    out = 0
    for i in factors(n):
        out += i
    return out
