import math

def TC():
    s = input()
    res = ""
    if len(s) % 2 != 0:
        for i in range(len(s) - 1):
            res += s[i]
    else:
        res = s
    a = []
    for i in range(0, len(res), 2): # 1 2 3 4 5
        x = int(res[i]) * 10 + int(res[i + 1])
        if not(x in a):
            a.append(x)

    for i in a:
        print(i, end = " ")

t = 1
#t = int(input())
for i in range(t): TC()





