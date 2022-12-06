import functools
from datetime import datetime

class LapHoaDon2 :
    def __init__(self, maKhachHang, tenKhachHang, soPhong, ngayNhanPhong, ngayTraPhong, tienDichVu):
        self.maKhachHang = "KH" +"{0:0>2}".format(maKhachHang)
        self.tenKhachHang = tenKhachHang
        self.soPhong = soPhong
        self.ngayNhanPhong = ngayNhanPhong
        self.ngayTraPhong = ngayTraPhong
        self.tienDichVu = tienDichVu
        self.tongTime = 0

    def tang(self):
        return self.soPhong[0:1]

    def donGiaTheoTang(self):
        if (self.tang() == "1"):
            return 25
        if (self.tang() == "2"):
            return 34
        if (self.tang() == "3"):
            return 50
        return 80

    def soNgayO(self):
        st1 = datetime.strptime(self.ngayTraPhong, "%d/%m/%Y")
        st2 = datetime.strptime(self.ngayNhanPhong, "%d/%m/%Y")
        return (st1 - st2).days + 1

    def tongTien(self):
        return self.soNgayO() * self.donGiaTheoTang() + self.tienDichVu

    def inRa(self):
        print(self.maKhachHang, self.tenKhachHang, self.soPhong, self.soNgayO(), self.tongTien())


def cmp(a, b):
    if a.tongTien() > b.tongTien():
        return -1
    return 1


n = int(input())
listKH = []
for i in range(n):
    s1 = input().strip()
    s2 = input().strip()
    s3 = input().strip()
    s4 = input().strip()
    s5 = int(input().strip())
    listKH.append(LapHoaDon2(i + 1, s1, s2, s3, s4, s5))

listKH = sorted(listKH, key=functools.cmp_to_key(cmp))
for i in listKH:
    i.inRa()

# 3
# Huynh Van Thanh
# 103
# 05/06/2010
# 05/06/2010
# 15
# Le Duc Cong
# 106
# 08/03/2010
# 01/05/2010
# 220
# Tran Thi Bich Tuyen
# 207
# 10/04/2010
# 21/04/2010
# 96
