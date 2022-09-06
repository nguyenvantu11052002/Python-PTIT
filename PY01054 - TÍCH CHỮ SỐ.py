import math

def TC () :
    s = input()
    res = 1
    for i in s:
        if i != '0' :
            res *= int(i)
    print(res)

t = 1
t = int(input())
for i in range (t) : TC()

# 2
# 123410
# 123456789123456789
