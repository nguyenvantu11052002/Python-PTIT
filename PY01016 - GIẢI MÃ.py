import math

def solve() :
    s = str(input())
    for i in range(0, len(s) - 1, 2) :
        for j in range(0, int(s[i + 1])) :
            print(s[i], end = '')
    print()
    
t = int(input())
for i in range (t) : solve()

