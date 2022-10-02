import math

a = [1] * 1000005

def sangnto():
    a[0] = 0
    a[1] = 0
    for i in range(2, int(math.sqrt(1000001)) + 1) :
        if a[i] == 1:
            for j in range(i * i, 1000002, i) :
                a[j] = 0

sangnto()
res = [0]
for i in range(1000001):
    if a[i] == 1:
        res += [i]

def TC () :
    n, x = [int(i) for i in input().split()]
    idx = 0
    for i in range(n + 1) :
        print(x + res[idx], end = " ")
        x = x + res[idx]
        idx += 1

t = 1
#t = int(input())
for i in range (t) : TC()

