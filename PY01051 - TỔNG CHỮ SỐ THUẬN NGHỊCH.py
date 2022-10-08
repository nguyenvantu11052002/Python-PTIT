import math

def tong(n) :
    res = 0
    for i in n:
        res += int(i)
    return res

def check(n):
    if tong(n) < 10: return False
    rv = str(tong(n))[::-1]
    return rv == str(tong(n))

def TC () :
    n = input()
    if check(n) :
        print("YES")
    else:
        print("NO")

t = 1
t = int(input())
for i in range (t) : TC()


# 2
# 12341
# 22222222222222222222
