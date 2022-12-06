import functools


class ThiSinh:
    def __init__(self, maThiSinh, tenThiSinh, diemLyThuyet, diemThucHanh):
        self.maThiSinh = "TS0" + "{0:0>1}".format(maThiSinh)
        self.tenThiSinh = tenThiSinh
        self.diemLyThuyet = diemLyThuyet
        self.diemThucHanh = diemThucHanh

    def DiemLyThuyet(self):
        if (self.diemLyThuyet > 10.0):
            return self.diemLyThuyet / 10.0
        return self.diemLyThuyet

    def DiemThucHanh(self):
        if (self.diemThucHanh > 10.0):
            return self.diemThucHanh / 10.0
        return self.diemThucHanh

    def tongDiem(self):
        return (self.DiemLyThuyet() + self.DiemThucHanh()) / 2

    def trangThai(self):
        if (self.tongDiem() > 9.5):
            return "XUAT SAC"
        if self.tongDiem() >= 8:
            return "DAT"
        if self.tongDiem() >= 5:
            return "CAN NHAC"
        return "TRUOT"

    def inRa(self):
        print(self.maThiSinh, self.tenThiSinh, "{:.2f}".format(self.tongDiem()), self.trangThai())


def cmp(a, b):
    if a.tongDiem() > b.tongDiem():
        return -1
    return 1


n = int(input())
listTS = []
for i in range(n):
    s1 = input()
    s2 = float(input())
    s3 = float(input())
    listTS.append(ThiSinh(i + 1, s1, s2, s3))

listTS = sorted(listTS, key=functools.cmp_to_key(cmp))
for i in listTS:
    i.inRa()

# 3
# Nguyen Thai Binh
# 45
# 75
# Le Cong Hoa
# 4
# 4.5
# Phan Van Duc
# 56
# 56
