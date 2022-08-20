def solve() :
    s = input()
    l = len(s)
    if (s[l - 1] == s[1] and s[l - 2] == s[0]) : print("YES")
    else: print("NO")

t = int(input())
for i in range (t) : solve()
