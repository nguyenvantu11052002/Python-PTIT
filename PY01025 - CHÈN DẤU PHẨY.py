import math

def solve() :
    s = input()
    n = len(s) - 1
    cnt = 0
    res = ""
    while 1:
        cnt += 1
        res = s[n] + res
        if (n == 0) : break
        if cnt == 3 :
            res = ',' + res
            cnt = 0
        n -= 1
    print(res)

t = 1
#t = int(input())
for i in range (t) : solve()

