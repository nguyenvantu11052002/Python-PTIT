import math

a = [0] * 100

def prepare():
    a[0] = 0
    a[1] = a[2] = 1
    for i in range(3, 93):
        a[i] = a[i - 1] + a[i - 2]

prepare()

def TC () :
    x, y = [int(i) for i in input().split()]
    for i in range(x, y + 1):
        print(a[i], end = " ")
    print()

t = 1
t = int(input())
for i in range (t) : TC()

# 2
# acxz
# bcxz
