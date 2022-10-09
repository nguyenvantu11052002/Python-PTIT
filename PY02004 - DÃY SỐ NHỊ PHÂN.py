import math

def solve(a, n):
    res = 0
    for i in range(n - 1):
        if a[i] != a[i + 1]: res += 1
    return res

def TC () :
    n = int(input())
    a = [int(i) for i in input().split()]
    print(solve(a, n))

t = 1
#t = int(input())
for i in range (t) : TC()

# 6
# 1 0 0 1 1 1
