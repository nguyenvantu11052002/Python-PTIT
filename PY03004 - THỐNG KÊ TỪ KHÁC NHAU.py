import math

def TC():
    f = {}
    n = int(input())
    for i in range(n):
        s = ""
        for j in input().lower() + ' ':
            if (j >= 'a' and j <= 'z') or (j >= '0' and j <= '9') :
                s += j
            else:
                if s != "":
                    if s in f: f[s] += 1
                    else: f[s] = 1
                    s = ""
    f = sorted(f.items(), key = lambda x: (-x[1], x[0]))
    for x in f:
        print(x[0], x[1])

t = 1
#t = int(input())
for i in range(t): TC()


# 3
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.
