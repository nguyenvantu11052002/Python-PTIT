import math

def solve() :
    s = str(input())
    cnt = 1
    for i in range(0, len(s) - 1, 1):
        if s[i] == s[i + 1] : cnt += 1
        else:
            print(cnt, s[i], sep = '', end = '')
            cnt = 1
    print(cnt, s[len(s) - 1], sep = '')

t = 1
t = int(input())
for i in range (t) : solve()

# 3
# AACDDPQ
# 11111147g
# 1111111111
