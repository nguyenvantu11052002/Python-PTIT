import math

def TC():
    n = int(input())
    a = [i for i in range(0, int(math.sqrt(n)) + 1)]
    i = 2
    while i * i <= int(math.sqrt(n)):
        if a[i] == i:
            for j in range(i * i, int(math.sqrt(n)) + 1, i):
                if a[j] == j:
                    a[j] = i
        i += 1

    res = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        p = a[i]
        q = a[i//p]
        if p * q == i and a[i] != i and p != q:
            res += 1
        elif a[i] == i:
            if i ** 8 <= n:
                res += 1
    print(res)

t = 1
#t = int(input())
for i in range(t): TC()




