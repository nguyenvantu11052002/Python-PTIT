import math

m = {1 : 1}

while True:
    a = []
    ok = False
    for i in m:
        if i < 10 ** 18:
            if not(i * 2 in m):
                a.append(i * 2)
            if not(i * 3 in m):
                a.append(i * 3)
            if not(i * 5 in m):
                a.append(i * 5)

    for i in a:
        m[i] = 1
        ok = True
    if ok == False: break

#m = sorted(m.items(), key = lambda x: x[0])
a = sorted(list(m))
index = 1
for i in a:
    m[i] = index
    index += 1

def TC():
    n = int(input())
    #print(n, "n day nay")
    if n in m:
        print(m[n])
    else:
        print("Not in sequence")

t = 1
t = int(input())
for i in range(t): TC()

# 11
# 1
# 2
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
