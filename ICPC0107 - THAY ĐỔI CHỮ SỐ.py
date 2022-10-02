import math

def TC () :
    m, n = [i for i in input().split()]
    a = min(m, n)
    b = max(m, n)
    s1 = input().strip()
    if s1.count(' '): s1, s2 = s1.split()
    else: s2 = input()
    res1 = int(s1.replace(b, a)) + int(s2.replace(b, a))
    res2 = int(s1.replace(a, b)) + int(s2.replace(a, b))
    print(res1, res2)

t = 1
t = int(input())
for i in range (t) : TC()

# 1
# 5 6
# 645
# 666
# 6 7
# 666
# 777
