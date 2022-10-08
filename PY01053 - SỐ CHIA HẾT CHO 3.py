import math

def check(n) :
    if int(n) % 3 == 0: return True
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
# 123456789123456789
