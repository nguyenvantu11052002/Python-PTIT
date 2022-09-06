import math

def TC () :
    s = input()
    s = s + 'z'
    res = 10**20

    tmp = 0
    ok = 0
    for i in s:
        if i.isdigit():
            tmp = tmp * 10 + int(i)
            ok = 1
        elif ok == 1:
            res = min(res, tmp)
            tmp = 0
            ok = 0
    print(res)


t = 1
t = int(input())
for i in range (t) : TC()

# 2
# 12ab29cd19
# ab123gh456cd
