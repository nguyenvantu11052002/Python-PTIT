import math

def TC():
    s = input()
    res = ""
    if len(s) % 2 != 0:
        for i in range(len(s) - 1):
            res += s[i]
    else:
        res = s
    m = {}
    for i in range(0, len(res), 2): # 1 2 3 4 5
        x = int(res[i]) * 10 + int(res[i + 1])
        if x in m:
            m[x] += 1
        else:
            m[x] = 1

    for i in m.items():
        print(i[0], i[1])


t = 1
#t = int(input())
for i in range(t): TC()





