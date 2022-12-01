import math

def TC():
    n = int(input())
    a = [float(x) for x in input().split()]
    maxele = 0.0
    minele = 10.0
    for i in a:
        maxele = max(maxele, i)
        minele = min(minele, i)
    res = []
    for i in a:
        if i != maxele and i != minele:
            res.append(i)
    ans = 0.0
    for i in res:
        ans += i
    print("{:.2f}".format(ans/len(res)))

t = 1
#t = int(input())
for i in range(t): TC()


# 6
# 6.75 8 9.2 7.25 7.75 6.75





