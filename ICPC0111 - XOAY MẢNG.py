import math

def TC () :
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    for i in range(k, n) :
        print(a[i], end = " ")
    for i in range(0, k) :
        print(a[i], end = " ")
    print()

t = 1
t = int(input())
for i in range (t) : TC()

# 2
# 5 2
# 1 2 3 4 5
# 10 3
# 2 4 6 8 10 12 14 16 18 20
