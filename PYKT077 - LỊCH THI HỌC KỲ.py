import functools
import math

class MonHoc:
    def __init__(self, maMon, tenMon):
        self.maMon = maMon
        self.tenMon = tenMon

class CaThi:
    def __init__(self, maCaThi, maMon, tenMon, ngayThi, gioThi, nhomThi):
        self.maCaThi = "T" + str.format("%03d" % maCaThi)
        self.maMon = maMon
        self.tenMon = tenMon
        self.ngayThi = ngayThi
        self.gioThi = gioThi
        self.nhomThi = nhomThi

    def inRa(self):
        print(self.maCaThi, self.maMon, self.tenMon, self.ngayThi, self.gioThi, self.nhomThi)

def chuyen(s):
    arr = s.strip().split("/")
    return arr[2] + arr[1] + arr[0]

def cmp(a, b):
    if chuyen(a.ngayThi) != chuyen(b.ngayThi):
        if chuyen(a.ngayThi) < chuyen(b.ngayThi):
            return -1
        return 1
    else:
        if a.gioThi != b.gioThi:
            if a.gioThi < b.gioThi:
                return -1
            return 1
        else:
            if a.maMon < b.maMon:
                return -1
            return 1

n, m = [int(x) for x in input().split()]
f = {}
for i in range(n):
    s1 = input().strip()
    s2 = input().strip()
    x = MonHoc(s1, s2)
    f[x.maMon] = x.tenMon

listRes = []
for i in range(m):
    arr = input().strip().split()
    x = CaThi(i + 1, arr[0], f[arr[0]], arr[1], arr[2], arr[3])
    listRes.append(x)

listRes = sorted(listRes, key = functools.cmp_to_key(cmp))
for i in listRes:
    i.inRa()

# 2 10
# INT1155
# Tin hoc co so 2
# INT1339
# Ngon ngu lap trinh C++
# INT1155 25/11/2021 08:00 01
# INT1155 04/12/2021 08:00 02
# INT1155 04/12/2021 13:30 03
# INT1155 25/11/2021 13:30 04
# INT1155 25/11/2021 15:00 05
# INT1339 25/11/2021 08:00 01
# INT1339 25/11/2021 08:00 02
# INT1339 04/12/2021 13:30 03
# INT1339 04/12/2021 13:30 04
# INT1339 04/12/2021 15:00 05


