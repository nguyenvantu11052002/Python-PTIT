import math
from itertools import permutations

s = input()
perm = permutations(s)
for i in list(perm):
    for j in i:
        print(j, end = "")
    print()




