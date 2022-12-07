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
    minele = 10**6
    for i in range(n):
        for j in range(m):
                maxele = max(maxele, a[i][j])
                minele = min(minele, a[i][j])

    res = maxele - minele
    kq = []
    kq.append(res)
    ok = False
    for i in range(n):
        for j in range(m):
            if a[i][j] == res:
                ok = True
                kq.append("Vi tri [" + str(i) + "][" + str(j) + "]")
    if ok:
        for i in kq:
            print(i)
    else:
        print("NOT FOUND")

t = 1
#t = int(input())
for i in range(t): TC()

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 67 28 23
# 29 77 11 67
# 16 51 24 21
# 13 25 77 77
