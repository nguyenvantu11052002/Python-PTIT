import math

def TC():
    n = int(input())
    a = []
    while True:
        tmp = [int(x) for x in input().split()]
        a += tmp
        if len(a) == n:
            break
    chan = []
    le = []
    for i in a:
        if i % 2 == 0:
            chan.append(i)
        else:
            le.append(i)
    chan = sorted(chan)
    le = sorted(le, reverse = True)
    index1 = 0; index2 = 0
    for i in a:
        if i % 2 == 0:
            print(chan[index1], end = " ")
            index1 += 1
        else:
            print(le[index2], end = " ")
            index2 += 1

t = 1
#t = int(input())
for i in range(t): TC()

# 10
# 1 2 3 4 5 6 7 7 9 6



