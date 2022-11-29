import math

def check(m, n):
    cnt = 0
    for i in m.items():
        if i[1] != 1 and i[1] != n - 1:
            return False
        else:
            if int(i[1]) == n - 1:
                cnt += 1
                if cnt > 1: return False
    if cnt != 1:
        return False
    return True

def TC():
    m = {}
    n = int(input())
    for i in range(n - 1):
        u, v = [int(x) for x in input().split()]
        if u in m:
            m[u] += 1
        else:
            m[u] = 1
        if v in m:
            m[v] += 1
        else: m[v] = 1
    if check(m, n):
        print("Yes")
    else:
        print("No")

t = 1
#t = int(input())
for i in range(t): TC()








