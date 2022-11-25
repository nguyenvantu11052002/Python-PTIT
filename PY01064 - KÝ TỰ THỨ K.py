import math

def TC() :
    n, k = [int(x) for x in input().split()]
    a = []
    for i in range (n) :
        a.append(pow(2, i))
    for i in range(n - 1, -1, -1):
        if k == a[i]:
            print(chr(i + 65))
        elif k > a[i]:
            k -= a[i]

t = 1
t = int(input())
for i in range(t) : TC()

# 2
# 3 2
# 4 8
