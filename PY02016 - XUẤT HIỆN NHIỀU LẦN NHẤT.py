import math

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    f = {}
    for i in a:
        if i in f : f[i] += 1
        else : f[i] = 1
    for i in f :
        if f[i] > int(n/2) :
            print(i)
            return
    print("NO")

t = 1
t = int(input())
for i in range(t) : solve()

# 2
# 9
# 3 3 4 2 4 4 2 4 4
# 8
# 3 3 4 2 4 4 2 4
