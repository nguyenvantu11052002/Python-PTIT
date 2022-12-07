import math

def TC():
    a, k, n = [int(x) for x in input().split()]
    ok = False
    for i in range(1, n + 1):
        aCongB = i * k
        if aCongB > n: break
        if aCongB <= n:
            if aCongB - a > 0:
                ok = True
                print(aCongB - a, end = " ")

    if ok == False:
        print(-1)

t = 1
#t = int(input())
for i in range(t): TC()
