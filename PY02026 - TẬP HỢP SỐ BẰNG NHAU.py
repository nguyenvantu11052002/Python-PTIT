import math

def check(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i] :
            return False
    return True

def TC():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    ain = []
    for i in a:
        if not(i in ain):
            ain.append(i)
    ain = sorted(ain)
    bin = []
    for i in b:
        if not(i in bin):
            bin.append(i)
    bin = sorted(bin)
    if check(ain, bin):
        print("YES")
    else:
        print("NO")

t = 1
#t = int(input())
for i in range(t): TC()

# 12 18
# 1 2 3 4 5 1 2 3 5 4 1 2
# 1 1 1 1 1 1 1 1 1 2 3 4 5 5 5 5 5 5



