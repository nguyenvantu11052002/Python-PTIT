import math

def check (n) :
    x = n
    m = 0
    while n != 0:
        m = m * 10 + n % 10
        n = int(n/10)
    if math.gcd(m, x) == 1 :
        return True
    return False

def TC () :
    n = int(input())
    if (check(n)) :
        print("YES")
    else:
        print("NO")

t = 1
t = int(input())
for i in range (t) : TC()

# 2
# acxz
# bcxz
