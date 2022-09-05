import math

def TC () :
    n = int(input())
    hang = [0] * n; cot = [0] * n
    for i in range(n) :
        s = input()
        for j in range(len(s)):
            if s[j] == 'C' :
                hang[i] += 1
                cot[j] += 1
    res = 0
    for i in range(n) :
        if hang[i] >= 2: res += math.comb(hang[i], 2)
        if cot[i] >= 2: res += math.comb(cot[i], 2)
    print(res)

t = 1
#t = int(input())
for i in range (t) : TC()

# 4
# CC..
# C..C
# .CC.
# .CC.
