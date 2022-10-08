import math

def check(n) :
    if len(n) < 3: return False
    id = 0
    for i in range(len(n) - 1):
        if n[i] == n[i + 1]: return False
        if int(n[i]) > int(n[i + 1]) :
            id = i
            break
    if id == len(n) - 2: return True
    for i in range(id, len(n) - 1) :
        if int(n[i]) <= int(n[i + 1]) :
            return False
    return True

def TC () :
    n = input()
    if check(n) :
        print("YES")
    else:
        print("NO")


t = 1
t = int(input())
for i in range (t) : TC()


# 3
# 12342
# 23342
# 5678961
