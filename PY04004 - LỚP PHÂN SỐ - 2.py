import math

class PhanSo:
    def __init__(self, tuSo, mauSo):
        self.tuSo = tuSo
        self.mauSo = mauSo

    def rutGon(self):
        ucln = math.gcd(self.tuSo, self.mauSo)
        self.tuSo //= ucln
        self.mauSo //= ucln
    def added(self, other):
        self.tuSo = self.tuSo * other.mauSo + other.tuSo * self.mauSo
        self.mauSo = self.mauSo * other.mauSo
    def output(self):
        print(self.tuSo, "/", self.mauSo, sep = "")

a, b, c, d = [int(x) for x in input().split()]
res1 = PhanSo(a, b)
res2 = PhanSo(c, d)
res1.added(res2)
res1.rutGon()
res1.output()


