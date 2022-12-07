import math

def TC():
    n = int(input())
    a = []
    while True:
        a += [int(x) for x in input().split()]
        if len(a) == n:
            break

    maxele = 0
    for i in a:
        maxele = max(maxele, i)

    ok = True
    for i in range(1, maxele + 1):
        if i not in a:
            ok = False
            print(i)
    if ok:
        print("Excellent!")

t = 1
#t = int(input())
for i in range(t): TC()
# 7
# 4 5 7 8 9
# 10 11
