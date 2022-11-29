import math

def TC():
    s = input()
    st = []
    cnt = 1
    for i in s:
        if i == '(':
            st.append(cnt)
            print(cnt, end = " ")
            cnt += 1
        elif i == ')':
            print(st[-1], end = " ")
            st.pop()
    print()

t = 1
t = int(input())
for i in range(t): TC()


# 2
# (a + (b *c) ) + (d/e)
# ( ( () ) ( () ) )




