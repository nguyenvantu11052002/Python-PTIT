import functools
import math

class Team:
    def __init__(self, maTeam, tenTeam, tenTruong):
        self.maTeam = "Team" + str.format("%02d" % maTeam)
        self.tenTeam = tenTeam
        self.tenTruong = tenTruong


class ThiSinh:
    def __init__(self, maThiSinh, hoVaTen, maTeam):
        self.maThiSinh = "C" + str.format("%03d" % maThiSinh)
        self.haVaTen = hoVaTen
        self.maTeam = maTeam

class Table:
    def __init__(self, maThiSinh, hoTen, tenTeam, tenTruong):
        self.hoTen = hoTen
        self.maThiSinh = maThiSinh
        self.tenTeam = tenTeam
        self.tenTruong = tenTruong

    def inRa(self):
        print(self.maThiSinh, self.hoTen, self.tenTeam, self.tenTruong)

def cmp(a, b):
    if a.hoTen < b.hoTen:
        return -1
    return 1

n = int(input())
m = {}
for i in range(n):
    s1 = input()
    s2 = input()
    x = Team(i + 1, s1, s2)
    m[x.maTeam] = x

listRes = []
n1 = int(input())
for i in range(n1):
    s1 = input()
    s2 = input()
    x = ThiSinh(i + 1, s1, s2)
    s3 = m[s2].tenTeam
    s4 = m[s2].tenTruong
    table = Table(x.maThiSinh, s1, s3, s4)
    listRes.append(table)

listRes = sorted(listRes, key = functools.cmp_to_key(cmp))
for i in listRes:
    i.inRa()

# 2
# BAV_MIS
# Banking Academy of Vietnam
# FTU Knights1
# Foreign Trade University
# 6
# Le Trung Toan
# Team01
# Nguyen Trinh Quoc Long
# Team01
# Giang Minh Tung
# Team01
# Nguyen Hang Giang
# Team02
# Nguyen Thanh Nhan
# Team02
# Nguyen Viet Duc
# Team02
