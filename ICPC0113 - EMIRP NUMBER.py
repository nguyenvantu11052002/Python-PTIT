import math
a = [1] * 1000005

def sangnto():
    a[0] = a[1] = 0
    for i in range(1001):
        if a[i]:
            for j in range(i * i, 1000001, i):
                a[j] = 0

sangnto()

def TC () :
    n = int(input())
    for i in range(1, n) :
        rv = int(str(i)[::-1])
        if rv > i and a[i] and a[rv] and rv < n:
            print(i, rv, end = " ")
    print()


t = 1
t = int(input())
for i in range (t) : TC()


