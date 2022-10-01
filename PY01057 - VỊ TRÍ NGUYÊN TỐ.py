import math

def nto(n) :
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0: return False
    return True

def check (n) :
    for i in range(len(n)) :
        if nto(i) :
            if nto(int(n[i])) == False: return False
        else:
            if nto(int(n[i])) :
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

# 2
# 14239567
# 2314514535353
