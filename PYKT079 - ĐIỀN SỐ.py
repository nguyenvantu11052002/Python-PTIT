import math

def TC():
    n = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a)
    l = a[0]
    r = a[-1]
    cnt = 0
    for i in range(l, r + 1):
        if not (i in a):
            cnt += 1
    print(cnt)

t = 1
t = int(input())
for i in range(t): TC()





