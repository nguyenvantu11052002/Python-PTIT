def solve () :
    s = input()
    res = "YES"
    for i in s:
        if i != '4' and i != '7' : res = "NO"
    print(res)
for i in range (int(input())) :
    solve()
