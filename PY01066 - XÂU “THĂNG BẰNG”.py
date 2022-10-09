import math

def check(s):
    sdao = s[::-1]
    for i in range(1,len(s)):
        if abs(ord(s[i]) -ord(s[i - 1])) != abs(ord(sdao[i]) - ord(sdao[i - 1])): return False
    return True

def TC () :
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")

t = 1
t = int(input())
for i in range (t) : TC()

# 2
# acxz
# bcxz
