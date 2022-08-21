import math

def check(s) :
    sum = 0
    for i in s:
        sum += int(i)
    if sum % 10 != 0:
        return 0
    for i in range(0, len(s) - 1, 1) :
        x = int(s[i]) - int(s[i + 1])
        if abs(x) != 2:
            return 0
    return 1

def solve() :
    s = str(input())
    if check(s) == 1:
        print("YES")
    else: print("NO")

t = 1
t = int(input())
for i in range (t) : solve()

# 3
# 1353
# 246864
# 123435
