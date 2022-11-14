import math

#bai nay input khong phai all deu la so, co ca ki tu nen khi ep sang int se IR

def check(arr) :
    if len(arr) != 4: return False
    for x in arr:
        if x.isdigit() :
            if int(x) > 255 or int(x) < 0: return False
        else: return False
    return True

def TC() :
    s = input()
    arr = s.split('.') # khong can dau [], no tu hieu arr la 1 mang
    if check(arr) :
        print("YES")
    else:
        print("NO")

t = 1
t = int(input())
for i in range(t) : TC()

# 2
# 192.168.1.1
# 256.255.255.255
