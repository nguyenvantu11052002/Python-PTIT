import math

def TC():
    n = int(input())
    a = [int(x) for x in input().split()]
    res1 = 10**10
    res2 = 0
    for i in a:
        sum = 0
        for j in a:
            sum += abs(i - j)
        if sum < res1:
            res1 = sum
            res2 = i
    print(res1, res2)

t = 1
#t = int(input())
for i in range(t): TC()


# 8
# 13 5 8 7 9 15 26 34

