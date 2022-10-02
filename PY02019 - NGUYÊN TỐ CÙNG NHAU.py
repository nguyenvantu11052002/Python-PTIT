import math

def TC () :
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    for i in range(n):
        for j in range(i + 1, n) :
            if math.gcd(a[i], a[j]) == 1:
                print(a[i], a[j], sep = " ")

t = 1
#t = int(input())
for i in range (t) : TC()

# 5
# 3 7 9 6 13
