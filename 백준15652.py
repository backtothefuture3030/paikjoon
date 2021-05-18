

a,b = map(int,input().split())
c=[]

def com(d,q,a,b):
    if d==b:
        print(' '.join(map(str,c)))
        return
    for i in range(q,a):
        c.append(i+1)
        com(d+1,i,a,b)
        c.pop()

com(0,0,a,b)

