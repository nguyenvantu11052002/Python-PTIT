import math

def check(s):
    s = s.lower()
    if s.endswith(".py"): return True
    return False

def TC () :
    s = input()
    if check(s):
        print("yes")
    else:
        print("no")

t = 1
#t = int(input())
for i in range (t) : TC()

# 2
# acxz
# bcxz
