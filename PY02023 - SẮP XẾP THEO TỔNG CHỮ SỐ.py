import functools
import math

def tongCS(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res

def cmp(a, b):
    if tongCS(a) != tongCS(b):
        if tongCS(a) < tongCS(b):
            return -1
        return 1
    else:
        if a < b:
            return -1
        return 1

def TC():
    n = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a, key = functools.cmp_to_key(cmp))
    for i in a:
        print(i, end = " ")
    print()

t = 1
t = int(input())
for i in range(t): TC()






