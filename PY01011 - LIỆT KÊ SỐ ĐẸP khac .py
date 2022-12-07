import math
import queue

def check(s):
    if s != s[::-1]:
        return False
    if len(s) % 2 != 0: #223322
        return False
    return True

def TC():
    n = int(input())
    q = queue.Queue()
    q.put("2")
    q.put("4")
    q.put("6")
    q.put("8")
    while q.qsize() > 0:
        s = q.get()
        if int(s) >= n:
            break
        if check(s):
            print(s, end = " ")
        q.put(s + "0")
        q.put(s + "2")
        q.put(s + "4")
        q.put(s + "6")
        q.put(s + "8")
    print()

t = 1
t = int(input())
for i in range(t): TC()
