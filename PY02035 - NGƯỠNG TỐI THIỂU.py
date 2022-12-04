import math

def TC():
    s = input()
    k = int(input())
    res = ""
    if len(s) % 2 != 0:
        for i in range(len(s) - 1):
            res += s[i]
    #print(res)
    else: res = s
    m = {}
    for i in range(0, len(res), 2):
        x = int(res[i]) * 10 + int(res[i + 1]) #1243
        if x in m:
            m[x] += 1
        else:
            m[x] = 1

    m = sorted(m.items(), key = lambda x: x[0])
    ok = False
    for i in m:
        if i[1] >= k:
            print(i[0], i[1])
            ok = True
    if ok == False:
        print("NOT FOUND")

t = 1
#t = int(input())
for i in range(t): TC()

# 124356141111434356149
# 2

# 124356141111434356149
# 10
