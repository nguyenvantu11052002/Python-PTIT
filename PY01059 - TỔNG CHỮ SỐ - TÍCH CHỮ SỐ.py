import math

def tong(s):
    res = 0
    for i in range(0, len(s), 2):
        res += int(s[i])
    return res

def solve(s):
    res = 1
    for i in range(1, len(s), 2):
        if int(s[i]) != 0:
            res *= int(s[i])
    return res

def tich(s):
    ok = False
    for i in range(1, len(s), 2):
        if int(s[i]) != 0:
            ok = True
            break
    if ok == False:
        return 0
    else:
        return solve(s)

def TC () :
    s = input()
    print(tong(s), tich(s))

t = 1
t = int(input())
for i in range (t) : TC()

# 3
# 12345678
# 20000
# 22334455667788
