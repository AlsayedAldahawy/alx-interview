#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0

    minOps = 0
    i = 0
    while i <= int((n ** 0.5)):

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                n //= i
                minOps += i
                break
    if minOps:
        return minOps

    return n
