import math

def nto(n) :
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0: return False
    return True

def socuoi(n) :
    m = 0
    for i in range(len(n) - 4, len(n)) :
        m = m * 10 + int(n[i])
    return m

def check (n) :
    if nto(socuoi(n)): return True
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
# 12234323130097
# 3443354654654654461123
# 43543543434554659999
