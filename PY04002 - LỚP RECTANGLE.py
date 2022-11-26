import math

class Rectangle:
    def __init__(self, w, h, cl):
        self.w = w
        self.h = h
        #self.cl = cl
        self.cl = cl[0:1].upper() + cl[1:].lower()
    def check(self):
        if self.w <= 0 or self.h <= 0: return False
        return True
    def output(self):
        if self.check() == False:
            print("INVALID")
        else:
            cv = (self.w + self.h) * 2
            dt = self.w * self.h
            print(cv, dt, self.cl)

a = input().split()
tmp = Rectangle(int(a[0]), int(a[1]), a[2])
tmp.output()
