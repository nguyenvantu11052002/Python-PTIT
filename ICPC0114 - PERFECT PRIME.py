import math

def nto (n) :
    if n < 2: return False
    for i in range (2, int(math.sqrt(n)) + 1) :
        if n % i == 0 :
            return False
    return True

def check (n) :
    if nto(n) == False: return False
    tong = 0
    m = 0
    while n != 0:
        d = n % 10
        if nto(d) == False:
            return False
        tong += d
        m = m * 10 + d
        n = int(n/10)
    if nto(m) == False or nto(tong) == False :
        return False
    return True

def TC () :
    n = int(input())
    if check(n) == True:
        print("Yes")
    else:
        print("No")

t = 1
t = int(input())
for i in range (t) : TC()

# 3
# 13
# 753
# 757
