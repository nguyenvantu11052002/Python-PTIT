import math
from decimal import Decimal


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, tmp):
        xres = self.x - tmp.x
        yres = self.y - tmp.y
        res = math.sqrt(xres ** 2 + yres ** 2)
        return "{:.4f}".format(res)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
# 2
# 0 0 0 5
# 0 199 5 6
