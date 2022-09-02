import math

def solve() :
    n, m, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    check, i, j, h = 0, 0, 0, 0
    while i < n and j < m and h < k:
        if a[i] == b[j] == c[h] :
            print(a[i], end = " ")
            i, j, h = i + 1, j + 1, h + 1
            check = 1
        elif a[i] < b[j]  : i += 1
        elif b[j] < c[h] : j += 1
        else : h += 1
    if check == 0:
        print("NO", end = "")
    print()

t = 1
t = int(input())
for i in range (t) : solve()


# 3
# 6 5 8
# 1 5 10 20 40 80
# 5 7 20 80 100
# 3 4 15 20 30 70 80 120
# 3 5 4
# 1 5 5
# 3 4 5 5 10
# 5 5 10 20
# 3 3 3
# 1 2 3
# 4 5 6
# 7 8 9
