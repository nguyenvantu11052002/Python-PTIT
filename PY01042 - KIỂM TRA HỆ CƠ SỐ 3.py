import math

def solve (s) :
    for i in s:
        if i != '0' and i != '1' and i != '2' : return 0
    return 1

def TC () :
    s = input()
    if solve(s) : print("YES")
    else: print("NO")


t = 1
t = int(input())
for i in range(t) : TC()

# 3
# 1214AB
# 10210221
# 22222222
