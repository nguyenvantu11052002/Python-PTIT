import math

def tn(n):
    if n < 10:
        return False
    s = str(n)
    return s == s[::-1]

def TC():
    n, m = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        tmp = [int(x) for x in input().split()]
        a.append(tmp)

    maxele = 0
    for i in range(n):
        for j in range(m):
            if tn(a[i][j]):
                maxele = max(maxele, a[i][j])
    if maxele != 0:
        print(maxele)
    for i in range(n):
        for j in range(m):
            if tn(a[i][j]) and a[i][j] == maxele:
                print("Vi tri [", i, "][", j, "]", sep = "")
    if maxele == 0:
        print("NOT FOUND")

t = 1
#t = int(input())
for i in range(t): TC()

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 29 28 23
# 29 77 11 19
# 16 26 24 21
# 13 25 77 77
