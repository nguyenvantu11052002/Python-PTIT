import math

adj = [[] for j in range(2)]
vs = []
n = 0; m = 0

def dfs(u):
    vs[u] = 1
    for i in adj[u]:
        if vs[i] == 0:
            dfs(i)

def tplt(u, n):
    vs.clear()
    for i in range(n + 1):
        vs.append(0)
    #print(len(vs), "lneeeeeee")
    vs[u] = 1
    res = 0
    for i in range(1, n + 1):
        if vs[i] == 0:
            res += 1
            dfs(i)
    return res

def TC():
    n, m = [int(x) for x in input().split()]
    adj.clear()
    for i in range(0, n + 1):
        adj.append([])
    vs.clear()
    for i in range(0, n + 1):
        vs.append(0)
    for i in range(m):
        u, v = [int(x) for x in input().split()]
        adj[u].append(v)
        adj[v].append(u)
    maxLienThong = 1
    kq = 0
    for i in range(1, n + 1):
        tmp = tplt(i, n)
        if tmp > maxLienThong:
            maxLienThong = tmp
            kq = i
    print(kq)

t = 1
t = int(input())
for i in range(t): TC()

# 2
# 5 5
# 1 2
# 1 3
# 2 3
# 3 4
# 3 5
# 5 7
# 1 2
# 1 3
# 2 3
# 2 5
# 3 4
# 3 5
# 4 5



