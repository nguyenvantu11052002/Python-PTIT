import math

def check(f):
    res = []
    for i in f:
        res.append(i[1])
    for i in range(len(res) - 1):
        if res[i] != res[i + 1]:
            return True
    return False

def TC():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    f = {}
    for i in a:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1

    f = sorted(f.items(), key = lambda x: (-x[1], x[0])) # 6 5 5 5 5 5 5 5
    ans = 0
    for i in f:
        ans = i[1]
        break

    if check(f):
        for i in f:
            if i[1] != ans:
                print(i[0])
                break
    else:
        print("NONE")

t = 1
#t = int(input())
for i in range(t): TC()

# 8 4
# 1 2 3 4 4 3 2 1

# 10 4
# 2 3 1 2 3 4 1 2 3 2
