import functools


class HocSinh:
    def __init__(self, maHocSinh, tenHocSinh, diem):
        self.maHocSinh = str.format("HS%02d" % maHocSinh)
        self.tenHocSinh = tenHocSinh
        self.diem = diem

    def diemTrungBinh(self):
        x = self.diem[0] * 2 + self.diem[1] * 2
        for i in range(2, 10):
            x += self.diem[i]
        return round(x * 100 + 1)/(100 * 12)

    def trangThai(self):
        if (self.diemTrungBinh() >= 9):
            return "XUAT SAC"
        if (self.diemTrungBinh() >= 8):
            return "GIOI"
        if (self.diemTrungBinh() >= 7):
            return "KHA"
        if (self.diemTrungBinh() >= 5):
            return "TB"
        return "YEU"

    def inRa(self):
        print(self.maHocSinh, self.tenHocSinh, str.format("%.1f" % self.diemTrungBinh()), self.trangThai())


def cmp(a, b):
    if a.diemTrungBinh() > b.diemTrungBinh():
        return -1
    return 1


n = int(input())
listHS = []
for i in range(n):
    s1 = input().strip()
    s2 = [float(x) for x in input().split()]
    listHS.append(HocSinh(i + 1, s1, s2))

listHS = sorted(listHS, key=functools.cmp_to_key(cmp))
for i in listHS:
    i.inRa()

# 3
# Luu Thuy Nhi
# 9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
# Le Van Tam
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
# Nguyen Thai Binh
# 9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
