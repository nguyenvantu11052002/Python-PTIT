import math

def nto (n) :
    if n < 2: return 0
    for i in range(2, int(n ** 0.5) + 1) :
        if n % i == 0: return 0
    return 1

def TC () :
    a = []
    n, m = map(int, input().split())
    for i in range(n) :
        a.append([int(i) for i in input().split()])

    for i in range(n) :
        for j in range(m) :
            print(nto(a[i][j]), end = " ")
        print()

t = 1
#t = int(input())
for i in range (t) : TC()

# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
