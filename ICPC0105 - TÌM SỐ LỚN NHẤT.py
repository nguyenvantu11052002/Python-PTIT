import math

def TC () :
    s = input()
    s = s + 'z'
    res = -1

    tmp = 0
    for i in s:
        if i.isdigit():
            tmp = tmp * 10 + int(i)
        else :
            res = max(res, tmp)
            tmp = 0
    print(res)


t = 1
t = int(input())
for i in range (t) : TC()

# 2
# 12ab29cd19
# ab123gh456cd
