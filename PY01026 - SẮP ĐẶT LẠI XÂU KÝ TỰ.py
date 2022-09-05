import math

def check(s1, s2) :
    if len(s1) != len(s2) : return 0
    for i in range(len(s1)) :
        if s1[i] != s2[i] : return 0
    return 1

def TC (x) :
    print("Test ", end = "")
    print(i + 1, end = ": ")
    s1 = list(input()); s2 = list(input())
    s1.sort(); s2.sort()
    if check(s1, s2) :
        print("YES")
    else: print("NO")


t = 1
t = int(input())
for i in range (t) : TC(i)

# 4
# testing
# intestg
# abc
# aabbbcccc
# abcabcbcc
# aabbbcccc
# abc
# xyz
