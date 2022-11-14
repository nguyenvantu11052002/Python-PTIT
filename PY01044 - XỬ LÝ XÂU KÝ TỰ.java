import math

def TC() :
    s1 = set(input().lower().split())
    s2 = set(input().lower().split())
    res1 = s1|s2
    res2 = s1&s2
    res1 = sorted(res1)
    res2 = sorted(res2)
    for x in res1:
        print(x, end = " ")
    print()
    for x in res2:
        print(x, end = " ")

t = 1
#t = int(input())
for i in range(t) : TC()

# Lap trinh huong doi tuong
# Ngon ngu lap trinh C++
