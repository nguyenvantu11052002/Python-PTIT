import math

def nto(n) :
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0: return False
    return True

def socuoi(n) :
    m = 0
    for i in range(len(n) - 3, len(n)) :
        m = m * 10 + int(n[i])
    return m

def sodau(n) :
    m = 0
    for i in range(3) :
        m = m * 10 + int(n[i])
    return m

def check (n) :
    if nto(socuoi(n)) and nto(sodau(n)): return True
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
# 12743
# 7337
# 12345678901234
