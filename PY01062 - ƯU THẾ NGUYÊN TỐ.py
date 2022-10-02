import math

def nto(n) :
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0: return False
    return True

def tongcsnt(n) :
    res = 0
    for i in n:
        if nto(int(i)) : res += 1
    return res

def check (n) :
    if nto(len(n)) and tongcsnt(n) > len(n) - tongcsnt(n): return True
    return False

def TC () :
    n = input()
    if check(n) :
        print("YES")
    else:
        print("NO")

t = 1
t = int(input())
for i in range (t) : TC()

# 3
# 1234567
# 22334455667
# 23400300489898989
