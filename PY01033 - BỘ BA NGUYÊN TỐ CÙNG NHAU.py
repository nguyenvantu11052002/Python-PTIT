import math

def check (i, j, k) :
    if math.gcd(i, j) != 1:
        return False
    if math.gcd(i, k) != 1:
        return False
    if math.gcd(j, k) != 1:
        return False
    return True

def TC () :
    l, r = map(int, input().split())
    for i in range(l, r - 1) :
        for j in range(i + 1, r) :
            for k in range(j + 1, r + 1) :
                if check(i, j, k) :
                    print("(", i, ", ", j, ", ", k, ")", sep = '')

t = 1
# t = int(input())
for i in range (t) : TC()

