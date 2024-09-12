#!/usr/bin/python3

"""
    the key to this problem is to realising that we cannot achieve any number by repeating other than its prime factors
"""
def minOperations(n):
    # if n <= 1:
    #     return 0
    # for i in range(2, int(n ** 0.5) + 1):
    #     if n % i == 0:
    #         return (i + minOperations(n // i))

    # return n
