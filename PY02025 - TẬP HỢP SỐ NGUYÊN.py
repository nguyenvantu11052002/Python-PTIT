import math

def solve() :
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort(); b.sort();
    seta = []; setb = []
    for i in a:
        if i not in seta:
            seta.append(i)
    for i in b:
        if i not in setb:
            setb.append(i)
    res1 = []; res2 = []; res3 = []
    for i in seta:
        if i in setb:
            res1.append(i)
        else: res2.append(i)
    for i in setb:
        if i not in seta:
            res3.append(i)
    for i in res1:
        print(i, end = " ")
    print()
    for i in res2:
        print(i, end = " ")
    print()
    for i in res3:
        print(i, end = " ")
    print()

t = 1
#t = int(input())
for i in range (t) : solve()


# 5 6
# 1 2 3 4 5
# 3 4 5 6 7 8
