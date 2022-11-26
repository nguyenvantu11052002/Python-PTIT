import math

class SoPhuc:
    def __init__(self, phanThuc, phanAo):
        self.phanThuc = phanThuc
        self.phanAo = phanAo

    def congHaiSoPhuc(self, other):
        res = SoPhuc(0, 0)
        res.phanThuc = self.phanThuc + other.phanThuc
        res.phanAo = self.phanAo + other.phanAo
        return res

    def nhanHaiSoPhuc(self, other):
        res = SoPhuc(0, 0)
        res.phanThuc = self.phanThuc * other.phanThuc - self.phanAo * other.phanAo
        res.phanAo = self.phanThuc * other.phanAo + self.phanAo * other.phanThuc
        return res

    def inSoPhuc(self):
        print(self.phanThuc, end = " ")
        if self.phanAo < 0:
            print("- ", self.phanAo * (-1), "i", sep = "", end = "")
        else:
            print("+ ", self.phanAo, "i", sep = "", end = "")

def TC():
    a, b, c, d = [int(x) for x in input().split()]
    A = SoPhuc(a, b)
    B = SoPhuc(c, d)
    C = A.congHaiSoPhuc(B).nhanHaiSoPhuc(A)
    D = A.congHaiSoPhuc(B).nhanHaiSoPhuc(A.congHaiSoPhuc(B))
    C.inSoPhuc()
    print(", ", end = "")
    D.inSoPhuc()
    print()

t = 1
t = int(input())
for i in range(t): TC()
