import math

def tichChuSo (n) :
    res = 1
    s = str(n)
    for i in s:
        res *= int(i)
    return res

def solve() :
    n = int(input())
    a = [int(i) for i in input().split()]
    for i in range (0, n - 1) :
        for j in range (i + 1, n) :
            if tichChuSo(a[j]) < tichChuSo(a[i]) or (tichChuSo(a[j]) == tichChuSo(a[i]) and a[j] < a[i]) :
                a[i], a[j] = a[j], a[i]
    for i in a :
        print(i, end = " ")
    print()

t = 1
t = int(input())
for i in range (t) : solve()


# 1
# 8
# 143 43 22 99 7 9 1111 10000000
