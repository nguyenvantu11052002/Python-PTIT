import functools
import math

class SinhVien:
    def __init__(self, name, ac, submit):
        self.name = name
        self.ac = ac
        self.submit = submit
    def inSinhVien(self):
        print(self.name, self.ac, self.submit)

def cmp(self, other):
    if self.ac != other.ac :
        if self.ac > other.ac: return -1
        return 1
    if self.submit != other.submit:
        if self.submit < other.submit: return -1
        return 1
    if self.name < other.name: return -1
    return 1

# def cmp(a, b) :
#     if a.ac < b.ac : return 1
#     elif a.ac == b.ac :
#         if a.submit > b.submit : return 1
#         elif a.submit == b.submit :
#             if a.name > b.name : return 1
#             else : return -1
#         else : return -1
#     else : return -1

def TC():
    n = int(input())
    listsv = []
    for i in range(n):
        name = input()
        ac, submit = [int(x) for x in input().split()]
        listsv.append(SinhVien(name, ac, submit))
    listsv = sorted(listsv, key = functools.cmp_to_key(cmp))
    for i in listsv:
        i.inSinhVien()

t = 1
#t = int(input())
for i in range(t): TC()

# 2
# Nguyen Van Nam
# 168 600
# Tran Thi Ngoc
# 169 600
