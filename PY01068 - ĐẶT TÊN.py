import math
from itertools import combinations

def TC():
    n, k = [int(x) for x in input().split()]
    arr = input().split()
    tmp = []
    for i in arr:
        if tmp.count(i) == 0:
            tmp.append(i)
    arr = tmp
    arr = sorted(arr)
    comb = combinations(arr, k)
    for i in list(comb):
        for j in i:
            print(j, end = " ")
        print()

t = 1
#t = int(input())
for i in range(t): TC()

# 6 2
# DONG TAY NAM BAC TAY BAC



