import math

def solve() :
    n = int(input())
    print("1", end = "")
    for i in range (2, int(n**0.5) + 1) :
        if n % i == 0 :
            cnt = 0
            while n % i == 0 :
                cnt += 1
                n //= i
            print(" * " + str(i) + "^" + str(cnt), end = "")
    if n > 1:
        print(" * " + str(n) + "^" + str(1), end = "")
    print()

t = 1
t = int(input())
for i in range (t) : solve()

# 3
# 28
# 100
# 1234
