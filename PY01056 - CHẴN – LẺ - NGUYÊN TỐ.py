import math

def nto(n) :
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0: return False
    return True

def tongcs (n) :
    sum = 0
    for i in n:
        sum += int(i)
    return sum

def check (n) :
    for i in range(len(n)) :
        if i % 2 == 0:
            if int(n[i]) % 2 != 0: return False
        else:
            if int(n[i]) % 2 == 0: return False
    if nto(tongcs(n)) == False: return False
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
# 2345678521
# 1212121212121212121212121
