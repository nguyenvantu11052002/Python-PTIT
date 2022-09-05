import math

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True :
    a = [str(i) for i in input().split()]
    k = int(a[0])
    if k == 0: break
    s1 = a[1]
    res = ""
    for i in s1 :
        index = s.find(i)
        res += s[(index + k) % 28]
    ans = list(res)
    ans.reverse()
    for i in ans:
        print(i, end = "")
    print()



# t = 1
# #t = int(input())
# for i in range (t) : TC()

# 1 ABCD
# 14 ROAD
# 0
