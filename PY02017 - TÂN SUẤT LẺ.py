import math

def TC () :
    n = int(input())
    a = [int(i) for i in input().split()]
    f = {}
    for i in a:
        if i in f:
            f[i] += 1
        else: f[i] = 1
    for i in a:
        if f[i] % 2 == 1:
            print(i)
            return

t = 1
t = int(input())
for i in range (t) : TC()

# 2
# 7
# 1 2 3 2 3 1 3
# 5
# 1 1 3 3 2
