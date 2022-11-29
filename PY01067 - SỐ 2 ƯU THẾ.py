import math
import queue

def TC():
    n = int(input())
    q = queue.Queue()
    q.put(["1", 0])
    q.put(["2", 1])
    res = []
    while t:
        tmp = q.get()
        #print(tmp[1], len(tmp[0]), "in ne")
        if tmp[1] > len(tmp[0])/2:
            res.append(tmp[0])
            n -= 1
            if n == 0: break
        q.put([tmp[0] + "0", tmp[1]])
        q.put([tmp[0] + "1", tmp[1]])
        q.put([tmp[0] + "2", tmp[1] + 1])
    for i in res:
        print(i, end = " ")
    print()

t = 1
t = int(input())
for i in range(t): TC()




