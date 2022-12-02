import math

def tim(a, n):
    maxele = 0
    for i in range(len(a)):
        maxele = max(maxele, a[i])
    for i in range(len(a)):
        if a[i] == maxele:
            return i
    return 0

def TC():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    vitri = tim(a, n)
    #print("vitri ", vitri)
    a.insert(vitri, m)
    am = []
    d = []
    for i in a:
        if i >= 0:
            d.append(i)
        else:
            am.append(i)
    for i in am:
        print(i, end = " ")
    for i in d:
        print(i, end = " ")
    print()

t = 1
t = int(input())
for i in range(t): TC()

# 1
# 5 3
# -1 2 2 4 -1



