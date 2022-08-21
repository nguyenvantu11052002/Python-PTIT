import math

def solve() :
    a, k, n = [int(i) for i in input().split()]
    ok = 0
    m = int(n / k)
    for i in range(1, m + 1, 1) :
        x = i * k - a
        if x > 0 :
            print(x, end = ' ')
            ok = 1
    if ok == 0: print(-1)

t = 1
for i in range (t) : solve()

