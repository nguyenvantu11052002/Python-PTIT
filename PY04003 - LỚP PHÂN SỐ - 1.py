import math

class PhanSo:
    def __init__(self, tuSo, mauSo):
        self.tuSo = tuSo
        self.mauSo = mauSo

    def solve(self):
        ucln = math.gcd(self.tuSo, self.mauSo)
        self.tuSo //= ucln
        self.mauSo //= ucln
    def output(self):
        print(self.tuSo, "/", self.mauSo, sep = "")

a, b = [int(x) for x in input().split()]
res = PhanSo(a, b)
res.solve()
res.output()
