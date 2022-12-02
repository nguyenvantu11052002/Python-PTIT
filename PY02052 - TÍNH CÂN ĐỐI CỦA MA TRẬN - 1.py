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
            if i < j:
                nuaTren += a[i][j]
            elif i > j:
                nuaDuoi += a[i][j]

    doChenhLech = abs(nuaTren - nuaDuoi)
    if doChenhLech <= k:
        print("YES")
    else:
        print("NO")
    print(doChenhLech)

t = 1
#t = int(input())
for i in range(t): TC()

# 5
# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9
# 5



