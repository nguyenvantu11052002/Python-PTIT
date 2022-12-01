import math

def TC():
    n = int(input())
    a = []
    for i in range(n):
        tmp = [int(x) for x in input().split()]
        a.append(tmp)
    #print(a)
    k = int(input())
    nuaTren = 0
    nuaDuoi = 0
    for i in range(n):
        for j in range(n):
            if i + j > n - 1:
                nuaDuoi += a[i][j]
            elif i + j < n - 1:
                nuaTren += a[i][j]
    dcl = abs(nuaTren - nuaDuoi)
    if dcl <= k:
        print("YES")
    else:
        print("NO")
    print(dcl)

t = 1
#t = int(input())
for i in range(t): TC()

# 5
# 2  8 10 6 7
# 6  3  2 6 9
# 10 2  6 2 8
# 9  9  7 9 8
# 9  6  5 6 9
# 5




