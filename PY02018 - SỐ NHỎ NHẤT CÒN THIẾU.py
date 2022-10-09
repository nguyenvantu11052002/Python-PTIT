import math

def check(a):
    for i in range(len(a) - 1):
        if a[i] + 1 != a[i + 1]: return False
    return True

def solve(a, n):
    for i in range(n):
        if a[i] != i + 1:
            return i + 1
    return n + 1

def TC():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    if check(a):
        print(a[n - 1] + 1)
    else:
        print(solve(a, n))


t = 1
#t = int(input())
for i in range(t): TC()





