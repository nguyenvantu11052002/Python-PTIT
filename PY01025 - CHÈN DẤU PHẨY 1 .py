import math

def TC():
    s = input()
    cnt = 0
    res = ""
    for i in range(len(s) - 1, -1, -1):
        cnt += 1
        res = s[i] + res
        if cnt % 3 == 0:
            res = "," + res

    if cnt % 3 == 0:
        res = res.lstrip(res[0])
    print(res)

t = 1
#t = int(input())
for i in range(t): TC()
