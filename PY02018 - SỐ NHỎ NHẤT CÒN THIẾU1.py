import math

def TC():
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in range(1, 30002):
        if not(i in a):
            print(i)
            break

t = 1
#t = int(input())
for i in range(t): TC()


# 3
# 1 2 4





