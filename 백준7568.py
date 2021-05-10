

def body():
    n = int(input())
    i=0
    q=[]
    w=[]
    r=[]
    while i<n:
        i+=1
        a,b = map(int,input().split())
        q.append(a)
        w.append(b)
    for i in range(len(q)):
        total=1
        for j in range(len(q)):
            if q[i]<q[j] and w[i]<w[j]:
                total+=1
        r.append(total)
    for i in r:
        print(i, end=' ')

body()
