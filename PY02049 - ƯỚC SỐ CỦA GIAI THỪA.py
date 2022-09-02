import math

def solve() :
    n, p = [int(i) for i in input().split()]
    res = 0
    x = 1
    while n > p**x :
        res += n// p**x
        x += 1
    print(res, end = "")
    print()

t = 1
t = int(input())
for i in range (t) : solve()


