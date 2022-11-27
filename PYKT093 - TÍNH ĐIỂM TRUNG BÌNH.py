import functools
import math

def rank(listDiem, x):
    for i in range(len(listDiem)):
        if listDiem[i] == x:
            return i + 1
    return -1

def lamTron(x): #6.625
    cuoi = int(x * 1000) % 10
    if cuoi >= 5:
        return math.ceil(x * 100)/100
    else:
        return math.floor(x * 100)/100

def chuanHoa(s):
    arr = s.split()
    res = ""
    for i in range(len(arr)):
        res += arr[i]
        if i != len(arr) - 1: res += " "
    return res

class ThiSinh:
    def __init__(self, maThiSinh, hoTen, diem1, diem2, diem3):
        self.maThiSinh = "SV{0:0>2}".format(maThiSinh)
        self.hoTen = chuanHoa(hoTen.title())
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3

    def diemTrungBinhDB(self):
        res = float((self.diem1 * 3  + self.diem2 * 3 + self.diem3 * 2)/8)
        return lamTron(res)

    def inThiSinh(self):
        print(self.maThiSinh, self.hoTen, "{:.2f}".format(self.diemTrungBinhDB()), end = " ")

def cmp(a, b):
    if a.diemTrungBinhDB() != b.diemTrungBinhDB():
        if a.diemTrungBinhDB() > b.diemTrungBinhDB():
            return -1
        return 1
    else:
        if a.maThiSinh < b.maThiSinh:
            return -1
        return 1

n = int(input())
thiSinh = []
listDiem = []
for i in range(n):
    s1 = input()
    s2 = float(input())
    s3 = float(input())
    s4 = float(input())
    tmp = ThiSinh(i + 1, s1, s2, s3, s4)
    listDiem.append(tmp.diemTrungBinhDB())
    thiSinh.append(tmp)

listDiem = sorted(listDiem, reverse= True)
thiSinh = sorted(thiSinh, key = functools.cmp_to_key(cmp))
for i in thiSinh:
    i.inThiSinh()
    print(rank(listDiem, i.diemTrungBinhDB()))

# 2
#  ha Thi kieu     anh
# 7
# 6
# 7
# Pham    THI  HAO
# 6
# 7
# 6


