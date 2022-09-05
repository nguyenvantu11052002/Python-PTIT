import math

def Try (n, res) :
    if n == 1 :
        print(res)
        return
    if n % 2 == 0:
        Try(n/2, res + 1)
    else: Try(3 * n + 1, res + 1)

while True :
    n = int(input())
    if n == 0: break
    Try (n , 1)

# t = 1
# #t = int(input())
# for i in range (t) : TC()

