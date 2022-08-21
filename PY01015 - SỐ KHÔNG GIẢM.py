import math

def solve() :
    n = input()
    res = "YES"
    for i in range(len(n) - 1) :
        if n[i] > n[i + 1] :
            res = "NO"
            break
    print(res)

t = int(input())
for i in range (t) : solve()

# 2
# 12345678888888888888889
# 65645645465754765876857685846
