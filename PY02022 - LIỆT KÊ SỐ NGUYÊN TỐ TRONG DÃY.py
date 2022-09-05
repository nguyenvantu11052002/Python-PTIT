import math

def nto (n) :
    if n < 2: return 0
    for i in range(2, int(n ** 0.5) + 1) :
        if n % i == 0: return 0
    return 1

def TC () :
    n = int(input())
    a = [int(i) for i in input().split()]
    f = {}

    for i in a:
        if i in f:
            f[i] += 1
        else: f[i] = 1
    for i in a:
        if nto(i) and f[i] > 0:
            print(i, f[i], sep = " ")
            f[i] = 0

t = 1
#t = int(input())
for i in range (t) : TC()

# 10
# 2 4 7 5 7 8 9 3 7 2
