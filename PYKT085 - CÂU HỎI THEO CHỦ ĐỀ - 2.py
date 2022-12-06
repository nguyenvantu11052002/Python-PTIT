import math

def TC():
    n = int(input())
    cnt = 0
    a = []
    while True:
        s = input()
        cnt += 1
        if s != "":
            a.append(s)
        else:
            print(a[0], ": ", len(a) - 1, sep = "")
            a.clear()
        if cnt == n: break
    print(a[0], ": ", len(a) - 1, sep = "")

t = 1
#t = int(input())
for i in range(t): TC()

# 9
# Home / accommodation
# Whatkindofhousing / accommodationdoyoulive in?
# Whodoyoulivewith?
# Howlonghaveyoulivedthere?
#
# Study
# Describeyoureducation
# What is yourareaofspecialization?
# Why did you choose to study that major?
