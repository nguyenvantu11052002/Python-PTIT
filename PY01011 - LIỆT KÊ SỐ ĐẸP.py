import math

def check(n) :
    n = str(n)
    if len(n) % 2 == 1 or n != n[::-1]: return 0
    for i in n:
        if int(i) % 2 == 1: return 0
    return 1

def TC () :
    n = int(input())
    for i in range(22, n, 2) :
        if check(i) :
            print(i, end = " ")
    print()




t = 1
t = int(input())
for i in range (t) : TC()

# 2
# 30
# 100
