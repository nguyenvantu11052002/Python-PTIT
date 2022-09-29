import math

def check (s) :
    x = ""
    for i in s: x = i + x
    for i in range (1, len(s)) :
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord (x[i]) - ord (x[i - 1])) :
                return False
    return True

def TC () :
    s = input()
    if check(s) :
        print("YES")
    else:
        print("NO")

t = 1
t = int(input())
for i in range (t) : TC()

# 2
# acxz
# bcxz
