import math
import queue

def TC():
    n, m = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        tmp = [int(x) for x in input().split()]
        a.append(tmp)
    vs = [[0 for i in range(m)] for j in range(n)]
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    res = 0
    q = queue.Queue()
    for i in range(n):
        for j in range(m):
            if a[i][j] == -1:
                q.put([i, j])
    while not q.empty():
        tmp = q.get()
        for i in range(8):
            x1 = tmp[0] + dx[i]
            y1 = tmp[1] + dy[i]
            if x1 >= 0 and x1 < n and y1 >= 0 and y1 < m and vs[x1][y1] == 0:
                vs[x1][y1] = 1
                res += a[x1][y1]

    print(res)

t = 1
#t = int(input())
for i in range(t): TC()





