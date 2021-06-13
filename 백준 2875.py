

w,m,i = map(int,input().split())
count = 0 

if w == 0 or m ==0 :
    print(0)
elif i==0:
    for j in range(1,m):
        if w==j*2:
            print(j)
elif w+m-2<i:
    print(0)
elif w>m*2:
    while w>m*2-i:
        if w<=m*2:
            m-=1
            count+=1
        else:
            w-=1
            count+=1
        if count==i:
            break
    #print(w,m)
    if w>=m*2:
        print(m)
else:  # w<=m*2
    if w<m:
        for k in range(1,m):
            if w%2==1:
                if w==k*2+1:
                    print(k)
                    exit()
            else:
                if w==k*2:
                    print(k)
                    exit()
    elif w>=m:
        for q in range(1,m):
            if w%2==1:
                if w==q*2+1:
                    print(q)
                    exit()
            else:
                if w==q*2:
                    print(q)
                    exit()
    while w<=m*2+i:
        if w<=m*2:
            m-=1
            count+=1
        else:
            w-=1
            count+=1
        if count == i:
            break
    #print(w,m)
    if w>=m*2:
        print(m)
'''

n, m, k = map(int, input().split())
count = 0
while n + m >= k and n >= 0 and m >= 0:
    n -= 2
    m -= 1
    count += 1
print(count - 1)
'''