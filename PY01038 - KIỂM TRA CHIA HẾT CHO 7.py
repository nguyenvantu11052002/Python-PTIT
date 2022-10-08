import math

def daonguoc(n) :
    m = 0
    while n != 0:
        m = m * 10 + n % 10
        n //= 10
    return m

def TC () :
    n = int(input())
    sum = 0
    if n % 7 == 0:
        print(n)
        return
    for i in range(1000) :
        sum += n + daonguoc(n)
        if sum % 7 == 0:
            print(sum)
            return
        n = sum
        sum = 0
    print(-1)

t = 1
t = int(input())
for i in range (t) : TC()


