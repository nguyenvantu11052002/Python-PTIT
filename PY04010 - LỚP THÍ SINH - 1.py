import math

class ThiSinh:
    def __init__(self, hoTen, ngaySinh, diem1, diem2, diem3):
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3

    def tongDiem(self):
        return "{:.1f}".format(self.diem1 + self.diem2 + self.diem3)

    def output(self):
        print(self.hoTen, self.ngaySinh, self.tongDiem())

s1 = input()
s2 = input()
s3 = float(input())
s4 = float(input())
s5 = float(input())
A = ThiSinh(s1, s2, s3, s4, s5)
A.tongDiem()
A.output()



# Nguyen Hoang Ha
# 11/10/2001
# 4.5
# 10.0
# 5.5
