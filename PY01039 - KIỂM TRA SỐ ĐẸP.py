import math

def check(n) :
    s = str(n)
    for i in range(0, len(s) - 2) :
        if s[i] != s[i + 2] :
            return False
    return True


def TC () :
    n = int(input())
    if (check(n)) :
        print("YES")
    else :
        print("NO")

t = 1
t = int(input())
for i in range (t) : TC()

# 3
# 12121212
# 343433
# 78789989
