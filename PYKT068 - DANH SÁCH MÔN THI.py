import functools
import math

class MonThi:
    def __init__(self, maMon, tenMon, hinhThucThi):
        self.maMon = maMon
        self.tenMon = tenMon
        self.hinhThucThi = hinhThucThi

    def inMonThi(self):
        print(self.maMon, self.tenMon, self.hinhThucThi)

def cmp(a, b):
    if a.maMon < b.maMon:
        return -1
    return 1

def TC():
    n = int(input())
    listMonThi = []
    for i in range(n):
        s1 = input()
        s2 = input()
        s3 = input()
        listMonThi.append(MonThi(s1, s2, s3))

    listMonThi = sorted(listMonThi, key= functools.cmp_to_key(cmp))
    for i in listMonThi:
        i.inMonThi()

t = 1
#t = int(input())
for i in range(t): TC()


# 2
# MUL1320
# Nhap mon da phuong tien
# Bai tap lon + Van dap truc tuyen
# BAS1203
# Giai tich 1
# Thi viet + Van dap truc tuyen





