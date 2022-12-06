import math

def TC():
    n = int(input())
    a = []
    for i in range(n):
        s = input()
        if s != "":
            a.append(s)
        else:
            print(a[0], ": ", len(a) - 1, sep = "")
            a.clear()
    print(a[0], ": ", len(a) - 1, sep = "")

t = 1
#t = int(input())
for i in range(t): TC()

