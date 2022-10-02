import math

def gt (n) :
    res = 1
    for i in range(n) :
        res *= (i + 1)
    return res

def tonggt(n) :
    res = 0
    while n != 0:
        res += gt(n % 10)
        n = int(n/10)
    return res

def check(n) :
    if n == tonggt(n) : return True
    return False

def TC () :
    n = int(input())
    if check(n) :
        print("Yes")
    else:
        print("No")

t = 1
t = int(input())
for i in range (t) : TC()


