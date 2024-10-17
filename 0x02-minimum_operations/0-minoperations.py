#!/usr/bin/python3

""" method that calculates the fewest number of operations
"""


def minOperations(n):
    """Function that calculates the fewest number of operations
    """

    val = 1
    start = 0
    counter = 0
    while val < n:
        remainder = n - val
        if (remainder % val == 0):
            start = val
            val += start
            counter += 2
        else:
            val += start
            counter += 1
    return counter
