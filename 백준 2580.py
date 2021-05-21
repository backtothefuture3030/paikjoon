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

 



'''
sk = [list(map(int, input().split())) for _ in range(9)]
z = [(i, j) for i in range(9) for j in range(9) if sk[i][j] == 0]

def percent(i, j):
    pro = [1,2,3,4,5,6,7,8,9]  
    
    for k in range(9):
        if sk[i][k] in pro:
            pro.remove(sk[i][k])
        if sk[k][j] in pro:
            pro.remove(sk[k][j])
            
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sk[p][q] in pro:
                pro.remove(sk[p][q])
    
    return pro

flag = False
def dfs(x):
    global flag
    
    if flag: 
        return
        
    if x == len(z): 
        for row in sk:
            print(*row)
        flag = True 
        return
        
    else:    
        (i, j) = z[x]
        pro = percent(i, j) 
        
        for num in pro:
            sk[i][j] = num 
            dfs(x + 1) 
            sk[i][j] = 0 
dfs(0)   

'''