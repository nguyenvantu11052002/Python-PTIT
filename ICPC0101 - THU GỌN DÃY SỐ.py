import math

def TC () :
    n = int(input())
    a = [int(i) for i in input().split()]
    b = []
    for i in a:
        if len(b) == 0:
            b.append(i)
        elif (i + b[-1]) % 2 == 0:
            b.pop()
        else:
            b.append(i)
    print(len(b))




t = 1
#t = int(input())
for i in range (t) : TC()

# 10
# 1 5 5 8 6 4 3 5 9 3
