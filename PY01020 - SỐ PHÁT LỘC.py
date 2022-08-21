import math

def check(s) :
    n = len(s)
    if s[n - 2] != '8' or s[n - 1] != '6': return 0
    return 1

def solve() :
    s = str(input())
    if check(s) == 1 :
        print("YES")
    else: print("NO")
 

t = int(input())
for i in range (t) : solve()

# 3
# 1539786
# 1234789
# 8686
