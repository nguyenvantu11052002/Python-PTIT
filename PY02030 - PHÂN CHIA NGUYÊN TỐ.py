import math

def nto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(a, n, x):
    res = 0
    for i in range(x + 1):
        res += a[i]
    if nto(res) == False:
        return False
    res = 0
    for i in range(x + 1, n):
        res += a[i]
    if nto(res) == False:
        return False
    return True

def TC():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = []
    for i in a:
        if not(i in b):
            b.append(i)
    n = len(b)
    ok = False
    for i in range(n):
        if check(b, n, i):
            print(i)
            ok = True
            break
    if ok == False:
        print("NOT FOUND")

t = 1
#t = int(input())
for i in range(t): TC()

# 10
# 3 6 7 3 5 7 3 6 6 7
