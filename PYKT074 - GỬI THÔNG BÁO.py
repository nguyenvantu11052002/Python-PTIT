import math

def TC():
    s = input()
    arr = s.split()
    #print(arr[6])
    if len(s) <= 100:
        print(s)
    else:
        res = ""
        a = []
        index = 0
        while len(res) <= 100:
            res += arr[index] + " "
            #print(res)
            a.append(arr[index])
           # print(index)
            index += 1

        a.pop()
        for i in a:
            print(i, end = " ")
    print()

t = 1
t = int(input())
for i in range(t): TC()





