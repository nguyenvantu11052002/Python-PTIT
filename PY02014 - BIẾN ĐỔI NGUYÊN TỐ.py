import math
nto = [1] * (10**6 + 5)

def sangnto():
    nto[0] = 0
    nto[1] = 0
    for i in range(2, 10 ** 3 + 1):
        if nto[i] == 1:
            for j in range(i * i, 10 ** 6 + 1, i):
                nto[j] = 0
sangnto()

def timCanTren(x):
    for i in range(x + 1, 10 ** 6 + 1, 1):
        if nto[i] == 1:
            return i

def timCanDuoi(x):
    for i in range(x - 1, 1, -1):
        if nto[i] == 1:
            return i

def TC():
    n = int(input())
    a = [int(x) for x in input().split()]
    res = 0
    for i in range(n):
        if nto[a[i]] == 0:
            res = max(res, min(timCanTren(a[i]) - a[i], a[i] - timCanDuoi(a[i])))
    print(res)


t = 1
#t = int(input())
for i in range(t): TC()


# 8
# 13 5 8 7 9 15 26 34
