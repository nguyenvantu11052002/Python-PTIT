import math

def xoay(s):
    sDau = s[0]
    sSau = s[1:]
    return sSau + sDau

def TC():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    res = 10**9
    ok = True
    s = a[0]
    for i in range(len(a[0])):
        cnt = 0
        for j in range(n): #noi lai cho nay cho ban hieu
            soLanXoay = len(a[j])
            s2 = a[j]
            while (s2 != s and soLanXoay > 0):
                cnt += 1
                s2 = xoay(s2)
                soLanXoay -= 1
            if s != s2:
                ok = False
                break
        res = min(res, cnt)
        s = xoay(s)

    if ok:
        print(res)
    else:
        print(-1)

t = 1
#t = int(input())
for i in range(t): TC()

# 3
# kc
# kc
# kc

# 2
# molzv
# lzvmo

# 4
# xzzwo
# zwoxz
# zzwox
# xzzwo

# 3
# aa
# aa
# ab
