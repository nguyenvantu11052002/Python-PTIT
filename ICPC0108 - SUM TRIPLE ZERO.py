import math

def TC() :
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    cnt = 0
    for i in range(n - 2) :
        l = i + 1
        r = n - 1
        while l < r:
            if (a[i] + a[l] + a[r] == 0) :
                cnt += 1
                l += 1
               # r -= 1
            elif (a[i] + a[l] + a[r] < 0) :
                l += 1
            else: r -= 1
    print(cnt)

t = 1
t = int(input())
for i in range(t) : TC()
# 2
# 5
# 0 -1 2 -3 1
# 5
# 1 -2  1  0  5
