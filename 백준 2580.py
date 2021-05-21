import sys

a = []
i = 0
w = 9
while i < w:
    i+=1
    a.append(list(map(int,sys.stdin.readline().split())))


for i in a:                   # 가로행 
    if 0 in i: 
        r = i.index(0)
        if len(set(i))==9 :
            i[r] = 45 - sum(i)

for j in range(9):           # 세로행
    t = []
    for i in a:
        t.append(i[j])
    if 0 in t:
        r = t.index(0)
        if len(set(t))==9:
            a[r][j]= 45 - sum(t)

# 3x3 정렬

y=3
t=0
z=3
while t<7:
    total=45
    c = []
    for i in range(t,z):
        for j in range(3):
            total-=a[i][j]
            if a[i][j]==0:
                c.append(i)
                c.append(j)
    if len(c)>=2:
        i = c[0]
        j = c[1]
        a[i][j] = total
    z+=3
    t+=3

y=3
t=0
z=3
while t<7:
    total=45
    c = []
    for i in range(t,z):
        for j in range(3,6):
            total-=a[i][j]
            if a[i][j]==0:
                c.append(i)
                c.append(j)
    if len(c)>=2:
        i = c[0]
        j = c[1]
        a[i][j] = total
    z+=3
    t+=3

y=3
t=0
z=3
while t<7:
    total=45
    c = []
    for i in range(t,z):
        for j in range(6,9):
            total-=a[i][j]
            if a[i][j]==0:
                c.append(i)
                c.append(j)
    if len(c)>=2:
        i = c[0]
        j = c[1]
        a[i][j] = total
    z+=3
    t+=3


# 출력

for i in a:
    for j in range(len(i)):
        print(i[j],end = " ")
    print()

 



