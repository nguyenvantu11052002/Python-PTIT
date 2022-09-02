import math

def solve() :
    n = int(input())
    a = []; le = []; chan = []

    while len(a) < n:
        a.extend(list(map(int, input().strip().split())))
    for x in a:
        if x % 2 == 0:
            chan.append(x)
        else: le.append(x)

    chan.sort(); le.sort(reverse= True)
    i1 = j1 = 0
    for i in a:
        if i % 2 == 0 :
            print(chan[i1], end = " ")
            i1 += 1
        else :
            print(le[j1], end = " ")
            j1 += 1
    print()

t = 1
#t = int(input())
for i in range (t) : solve()

# 10
# 1 2 3 4 5 6 7 7 9 6
