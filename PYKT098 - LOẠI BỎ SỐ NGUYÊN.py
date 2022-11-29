import math

def checkSo(s):
    res = 0
    for i in s:
        if i.isdigit():
            res += 1
        else:
            return False
    return True

def check(s):
    res = 0
    if checkSo(s):
        for i in s:
            res = res * 10 + int(i)
            if res > 2147483647 or res < -2147483648: return True
        return False
    return True

def TC():
    file = open("DATA.in", "r")
    listkq = []
    for line in file:
        for s in line.split():
            if check(s):
                listkq.append(s)
    listkq = sorted(listkq)
    for i in listkq:
        print(i, end = " ")
    print()

t = 1
#t = int(input())
for i in range(t): TC()



