import math

def TC () :
    n = int(input())
    a = [int(i) for i in input().split()]
    res = 0
    for i in range (n - 1) :
        for j in range (i + 1, n) :
            if a[i] > a[j] : res += 1
    print(res)

t = 1
#t = int(input())
for i in range (t) : TC()

# 5
# 2 4 1 3 5
