#!/usr/bin/python3

"""
    * the key to this problem is to realising that we cannot achieve any number
      by repeating other than its prime factors.
    * therefor we should be cautious with using "Copy All" so that we don't have number that
      can't reach the desired n by repetition.
    
    EX: n = 26
    should do:
        H >cpyall>paste -> 2 -> paste> paste> ... 13 times paste
    
    shouldn't do:
        H >cpyall>paste -> 2 >cpyall>paste -> 4 .....
        now we will be stucked because we can't achieve 26 by repeating 4.
"""


def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while divisor * divisor <= n:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    if n > 1:
        operations += n
    
    return operations
