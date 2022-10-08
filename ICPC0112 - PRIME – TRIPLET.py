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
    cnt = 0
    for i in range(n - 6):
        if a[i] and a[i + 2] and a[i + 6] or a[i] and a[i + 4] and a[i + 6]:
            cnt += 1
    print(cnt)

t = 1
t = int(input())
for i in range (t) : TC()


# 2
# 12341
# 22222222222222222222
