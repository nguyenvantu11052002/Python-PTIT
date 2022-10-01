import math

def TC () :
    n, k = [int(i) for i in input().split()]
    st = pow(10, k - 1)
    ed = pow(10, k) - 1
    cnt = 0
    for i in range(st, ed + 1) :
        if math.gcd(n, i) == 1:
            print(i, end = " ")
            cnt += 1
            if cnt % 10 == 0:
                print()

t = 1
# t = int(input())
for i in range (t) : TC()

# 2
# acxz
# bcxz
