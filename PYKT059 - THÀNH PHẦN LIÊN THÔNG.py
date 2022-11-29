import math

adj = [[] for j in range(2)]
vs = []

def dfs(u):
    vs[u] = 1
    for i in adj[u]:
        if vs[i] == 0:
            dfs(i)

def TC():
    n, m, x = [int(x) for x in input().split()]
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
    dfs(x)
    for i in range(1, n + 1):
        if vs[i] == 0:
            print(i)

t = 1
#t = int(input())
for i in range(t): TC()

# 6 4 2
# 1 3
# 2 3
# 1 2
# 4 5



