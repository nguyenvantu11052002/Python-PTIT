import math

def Try(s, n, a, b, c) :
    if (len(s) == n and a > 0 and a <= b and b <= c) : print(s)
    elif len(s) < n:
        Try(s + "A", n, a + 1, b, c)
        Try(s + "B", n, a, b + 1, c)
        Try(s + "C", n, a, b, c + 1)

def TC() :
    n = int(input())
    for i in range(3, n + 1) :
        Try("", i, 0, 0, 0)

t = 1
#t = int(input())
for i in range(t) : TC()
