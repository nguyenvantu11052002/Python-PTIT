import math

def solve():
    b = []
    res = []
    n = int(input())

    for i in range (n) :
        b.append([int(j) for j in input().split()])

    if n == 2 :
        print(1, b[0][1] - 1)
        return
    res.append((b[0][1] + b[0][2] - b[1][2]) // 2)

    for i in range(1, n) :
        res.append(b[0][i] - res[0])
    for i in range(n) :
        print(res[i], end = " ")

t = 1
#t = int(input())
for i in range(t) : solve()

# 4
# 0 3 6 7
# 3 0 5 6
# 6 5 0 9
# 7 6 9 0
