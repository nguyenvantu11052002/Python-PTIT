import math

def TC () :
    n = int(input())
    f = {}
    for i in range(n) :
        x = int(input())
        if x in f: f[x] += 1
        else : f[x] = 1
    maxx = 0
    for i in f:
        maxx = max(maxx, f[i])
    res = 1001
    for i in f:
        if f[i] == maxx: res = min(res, int(i))
    print(res)

t = 1
t = int(input())
for i in range (t) : TC()

# 3
# 3
# 999
# 999
# 19
# 4
# 13
# 333
# 333
# 13
# 3
# 11
# 12
# 13
