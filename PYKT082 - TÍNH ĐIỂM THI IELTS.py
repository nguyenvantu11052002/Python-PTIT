import math

def solve(x) :
    if (x >= 39) : return 9.0
    if (x >= 37) : return 8.5
    if x >= 35 : return 8.0
    if x >= 33: return 7.5
    if x >= 30: return 7.0
    if x >= 27: return 6.5
    if x >= 23: return 6.0
    if x >= 20: return 5.5
    if x >= 16: return 5.0
    if x >= 13: return 4.5
    if x >= 10: return 4.0
    if x >= 7: return 3.5
    if x >= 5: return 3.0
    if x >= 3: return 2.5

def lamTron(x) :
    if x >= int(x) + 0.75 : return int(x) + 1.0
    if x >= int(x) + 0.25 : return int(x) + 0.5
    return int(x) + 0.0

def TC() :
    x, y, c, d = [float(x) for x in input().split()]
    a = solve(x)
    b = solve(y)
    tb = (a + b + c + d)/4.0
    print(lamTron(tb))

t = 1
t = int(input())
for i in range(t) : TC()

# 2
# 15 25 5.0 5.5
# 22 32 6.0 6.0
