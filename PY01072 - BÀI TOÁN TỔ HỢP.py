import math
from itertools import combinations

n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = []
for i in a:
    if b.count(i) == 0:
        b.append(i)
b.sort()
a = b

comb = combinations(a, k)
for i in list(comb):
    for j in i:
        print(j, end = " ")
    print()

# 8 3
# 2 4 4 3 5 1 3 4



