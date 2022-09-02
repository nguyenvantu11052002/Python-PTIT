import math

def solve():
    res = ""
    n, b = map(int, input().split())
    while n > 0:
        du = n % b
        if du >= 10 : res += str(chr(du + 55))
        else : res += str(du)
        n //= b
    print("".join(reversed(res)))

t = 1
t = int(input())
for i in range(t) : solve()

# 3
# 10 2
# 2021 2
# 31 16
