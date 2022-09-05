import math

def nto (n) :
    if n < 2: return 0
    for i in range(2, int(n ** 0.5) + 1) :
        if n % i == 0: return 0
    return 1

def TC () :
    s = input()
    n = len(s)
    res = s[n - 4 : n]
    ans = int(res)

    if nto(ans) :
        print("YES")
    else: print("NO")

t = 1
t = int(input())
for i in range (t) : TC()

# 3
# 12234323130097
# 3443354654654654461123
# 43543543434554659999
