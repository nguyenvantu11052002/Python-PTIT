import math

def check(s):
    if len(s) % 2 == 0: return False
    if s[0] == s[1] : return False
    for i in range(0, len(s) - 2, 2) :
        if s[i] != s[i + 2] :
            return False
    return True

def TC () :
    s = input()
    if check(s) :
        print("YES")
    else:
        print("NO")

t = 1
t = int(input())
for i in range (t) : TC()

# 2
# 2324272921262
# 13141516
