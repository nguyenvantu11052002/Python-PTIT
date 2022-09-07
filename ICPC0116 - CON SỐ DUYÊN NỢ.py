import math

def check(n) :
    if n[0] != n[-1] : return 0
    return 1

def TC () :
    n = input()
    if check(n) :
        print("YES")
    else: print("NO")

t = 1
t = int(input())
for i in range (t) : TC()

