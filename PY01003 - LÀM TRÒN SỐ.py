import math

def TC () :
    arr = list(int(i) for i in input())
    for i in range(len(arr) - 1, 0, -1) :
        if arr[i] >= 5:
            arr[i - 1] += 1
        arr[i] = 0
    for i in arr:
        print(i, end = '')
    print()

t = 1
t = int(input())
for i in range (t) : TC()

# 7
# 15
# 14
# 5
# 99
# 12345678
# 44444445
# 1445
