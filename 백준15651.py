

a,b = map(int,input().split())
c=[]

def com(d,a,b):
    if d==b:
        print(' '.join(map(str,c)))
        return
    for i in range(a):
        c.append(i+1)
        com(d+1,a,b)
        c.pop()

com(0,a,b)

