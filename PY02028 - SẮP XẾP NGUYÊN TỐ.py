import math

def nto(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def TC():
    n = int(input())
    a = [int(x) for x in input().split()]

    mangnto = []
    mangkhongnto = []
    for i in a:
        if nto(i):
            mangnto.append(i)
        else:
            mangkhongnto.append(i)

    mangnto = sorted(mangnto)
    index1 = 0
    index2 = 0
    for i in a:
        if nto(i):
            print(mangnto[index1], end = " ")
            index1 += 1
        else:
            print(mangkhongnto[index2], end = " ")
            index2 += 1

t = 1
#t = int(input())
for i in range(t): TC()



# 8
# 4 6 3 8 7 2 5 9
