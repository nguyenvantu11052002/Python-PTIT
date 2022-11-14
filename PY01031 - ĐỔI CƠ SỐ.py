import math

def TC() :
    n, k = [int(x) for x in input().split()]
    s = ""
    while(True) :
        du = n % k
        if du >= 10:
            s += chr(du + 55)
        else: s += str(du)
        n //= k
        if n == 0: break
    s = s[::-1]
    print(s)

t = 1
t = int(input())
for i in range(t) : TC()

# 3
# 10 2
# 2021 2
# 31 16
