import math

def nto(n) :
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0: return False
    return True

def tongcs (n) :
    sum = 0
    for i in n:
        sum += int(i)
    return sum

def check (n) :
    if nto(tongcs(n)): return True
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

# 2
# 12341
# 22222222222222222222
