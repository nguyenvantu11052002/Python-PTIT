import math

def TC():
    n, m = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        tmp = [int(x) for x in input().split()]
        a.append(tmp)
    if n > m:
        #loai bo nhung hang co thu tu chan
        soHangCanLoaiBo = n - m
        for i in range(n):
            if i % 2 == 0 and soHangCanLoaiBo > 0:
                soHangCanLoaiBo -= 1
                continue
            else:
                for j in range(m):
                    print(a[i][j], end = " ")
                print()
    else:
        #loai bo nhung cot le
        res = []
        soCotCanLoaiBo = m - n
        for i in range(m):
            if i % 2 == 1 and soCotCanLoaiBo > 0:
                soCotCanLoaiBo -= 1
                continue
            else:
                tmp = []
                for j in range(n):
                    tmp.append(a[j][i])
                res.append(tmp)
        for i in range(n):
            for j in range(n):
                print(res[j][i], end = " ")
            print()

t = 1
#t = int(input())
for i in range(t): TC()

# 4 6
# 2 8 7 6 4 3
# 6 3 2 6 7 2
# 7 2 2 8 9 1
# 9 9 9 8 0 7
