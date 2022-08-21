import math
def nto(n) :
    if n < 2: return 0
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0: return 0
    return 1

def solve() :
    n = int(input())
    cnt = 0
    for i in range (n) :
        if math.gcd(i, n) == 1: cnt += 1
    if nto(cnt) == 1: print("YES")
    else: print("NO")

t = int(input())
for i in range (t) : solve()
