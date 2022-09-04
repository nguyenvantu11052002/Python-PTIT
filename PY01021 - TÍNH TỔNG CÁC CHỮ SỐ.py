import math

def solve() :
    s = list(input())
    s.sort()
    res = ""
    so = 0;
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9' :
            so += int(s[i])
        else: res += s[i]
    res += str(so)
    print(res)

t = 1
t = int(input())
for i in range (t) : solve()


