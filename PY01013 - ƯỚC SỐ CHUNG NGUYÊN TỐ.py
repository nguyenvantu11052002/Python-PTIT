import math
def nto(n) :
    if n < 2: return 0
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0: return 0
    return 1

def solve() :
    a, b = map(int, input().split())
    c = str(math.gcd(a, b))
    sum = 0
    for i in c :
        sum += int(i)
    if nto(sum) == 1:
        print("YES")
    else: print("NO")

t = int(input())
for i in range (t) : solve()

# 3
# 28 42
# 123 18
# 550 55
