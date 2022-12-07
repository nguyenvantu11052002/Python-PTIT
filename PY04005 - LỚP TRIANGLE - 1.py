import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def khoangCach(self, other):
        xres = other.x - self.x
        yres = other.y - self.y
        res = math.sqrt(xres ** 2 + yres ** 2)
        return res

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check(self):
        ab = self.a.khoangCach(self.b)
        bc = self.b.khoangCach(self.c)
        ca = self.c.khoangCach(self.a)
        if ab + bc <= ca or ab + ca <= bc or bc + ca <= ab:
            return False
        return True

    def chuVi(self):
        ab = self.a.khoangCach(self.b)
        bc = self.b.khoangCach(self.c)
        ca = self.c.khoangCach(self.a)
        res = ab + bc + ca
        return str.format("%.3f" % res)

    def inRa(self):
        print(self.chuVi())

a = []
t = 1
t = int(input())
for i in range (t):
    a += [float(x) for x in input().split()]
i = 0
for x in range(t):
    tmp = Triangle(Point(a[i], a[i + 1]), Point(a[i + 2], a[i + 3]), Point(a[i + 4], a[i + 5]))
    if tmp.check():
        tmp.inRa()
    else:
        print("INVALID")
    i += 6

# 3
# 0 0 0 5 0 199
# 1 1 1 1 1 1
# 0 0 0 5 5 0
