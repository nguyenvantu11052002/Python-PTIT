import math
def solve() :
    n, x, m = [float(i) for i in input().split()]
    y = math.log(m/n, 1 + x/100)
    if y == int(y) :
        print(y)
    else: print(int(y + 1))

t = int(input())
for i in range (t) : solve()

