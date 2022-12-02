import math



def TC():
    n = int(input())
    a = [int(x) for x in input().split()]
    st = []
    l = [0] * n
    for i in range(n):
        while len(st) > 0 and a[i] >= a[st[-1]]:
            st.pop()
        if len(st) == 0:
            l[i] = 0
        else:
            l[i] = st[-1] + 1
        st.append(i)

    for i in range(n):
        print(i - l[i] + 1, end = " ")
    print()

t = 1
t = int(input())
for i in range(t): TC()


# 1
# 7
# 100 80 60 70 60 75 85



