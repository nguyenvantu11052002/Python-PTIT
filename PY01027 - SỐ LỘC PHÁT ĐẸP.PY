import math

def check (s) :
    a = [int(i) for i in s]
    if a[0] == 8: return 0
    if a[0] != 6 and a[0] != 8: return 0
    cnt = 0
    for i in range(1, len(a)):
        if a[i] != 6 and a[i] != 8: return 0
        if a[i] == 8: cnt += 1
        else: cnt = 0
        if cnt > 2 : return 0
    return 1

def solve() :
    s = input()
    if (check(s)): print("YES")
    else: print("NO")

t = 1
#t = int(input())
for i in range (t) : solve()

