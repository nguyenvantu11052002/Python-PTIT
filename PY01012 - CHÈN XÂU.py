import math


def TC (x) :
    s1 = input()
    s2 = input()
    p = int(input())
    for i in range(0, p - 1) :
        print(s1[i], end = "")
    print(s2, end = "")
    for i in range(p - 1, len(s1)) :
        print(s1[i], end = "")


t = 1
#t = int(input())
for i in range (t) : TC(i)


# mon thcs2 hoc de
# ngon ngu C.
# 1
