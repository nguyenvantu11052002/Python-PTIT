import functools

def chuanHoa(s):
    arr = s.strip().split()
    res = ""
    for i in arr:
        res += i + " "
    return res.strip()

class KhachHang:
    def __init__ (self, maKhachHang, tenKhachHang, loaiHoGD, chiSoDau, chiSoCuoi):
        self.maKhachHang = "KH" + str.format("%02d" % maKhachHang)
        self.tenKhachHang = chuanHoa(tenKhachHang).title()
        self.loaiHoGD = loaiHoGD
        self.chiSoDau = chiSoDau
        self.chiSoCuoi = chiSoCuoi
        
    def dinhMuc(self):
        if self.loaiHoGD == "A":
            return 100
        if self.loaiHoGD == "B":
            return 500
        return 200
    
    def tienTrongDinhMuc(self):
        res = self.chiSoCuoi - self.chiSoDau
        if res < self.dinhMuc():
            return res * 450
        return self.dinhMuc() * 450
    
    def tienVuotDinhMuc(self):
        res = self.chiSoCuoi - self.chiSoDau
        if res > self.dinhMuc():
            return (res - self.dinhMuc()) * 1000
        return 0
    
    def thueVAT(self):
        return self.tienVuotDinhMuc() // 20
    
    def tienPhaiNop(self):
        return self.tienTrongDinhMuc() + self.tienVuotDinhMuc() + self.thueVAT()
    
    def inRa(self):
        print(self.maKhachHang, self.tenKhachHang, self.tienTrongDinhMuc(), self.tienVuotDinhMuc(), self.thueVAT(), self.tienPhaiNop())
        
def cmp(a,b):
    if a.tienPhaiNop() > b.tienPhaiNop():
        return -1
    return 1

n = int(input())
listKH = []
for i in range(n):
    s1 = input().strip()
    s2 = input().strip().split()
    x = KhachHang(i + 1, s1, s2[0], int(s2[1]), int(s2[2]))
    listKH.append(x)
    
listKH = sorted(listKH, key = functools.cmp_to_key(cmp))
for i in listKH:
    i.inRa()
    
# 2
# nGuyEn Hong Ngat
# C 200 278
# Chu thi    minh
# A 120 160

