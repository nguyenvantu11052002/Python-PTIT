import math

def TC():
    n = int(input())
    a = []
    for i in range(n):
        arr = input().split()
        a.append(len(arr))

    for i in range(len(a)):
        if a[i] == 6:
            a[i] = 8

    kq = []
    res = 0 #dem so bai tho 68
    ok8 = True
    for i in range(len(a)): #8888 7777 7777 888888
        if a[i] == 8 and ok8 == True:
            res += 1
            ok8 = False
        else:
            if a[i] == 7 :
                ok8 = True
    print(res + int(a.count(7) / 4))

    ok8 = True
    cnt = 0
    for i in range(len(a)):
        if a[i] == 8 and ok8 == True:
            if cnt > 0:
                soBai = cnt//4
                for j in range(soBai):
                    kq.append(2)
            kq.append(1)
            ok8 = False
            cnt = 0
        else:
            if a[i] == 7:
                cnt += 1
                ok8 = True
    if cnt > 0:
        soBai = cnt // 4
        for j in range(soBai):
            kq.append(2)
    for i in kq:
        print(i)

t = 1
#t = int(input())
for i in range(t): TC()

# 12
# Minh ve minh co nho ta
# Muoi lam nam ay thiet tha man nong
# Minh ve minh co nho khong
# Nhin cay nho nui nhin song nho nguon
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay



