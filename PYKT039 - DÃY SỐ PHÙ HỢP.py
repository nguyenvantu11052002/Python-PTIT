import math

def check(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    return True

def TC():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a = sorted(a)
    b = sorted(b)
    if check(a, b):
        print("YES")
    else:
        print("NO")

t = 1
t = int(input())
for i in range(t): TC()

# 2
# 4
# 7 5 3 2
# 5 4 8 7
# 8
# 7 5 3 2 5 105 45 10
# 2 4 0 5 6 9 75 84




