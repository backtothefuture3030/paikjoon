import sys

a,b = map(int,sys.stdin.readline().split())
w = 0
c = []
while w<a:
    w+=1
    c.append(int(sys.stdin.readline()))

c.sort(reverse=True)
count=0
for i in c:
    if (b//i)>1:
        count+=(b//i)
        b-=((b//i)*i)
    elif (b//i)==1:
        count+=(b//i)
        b-=((b//i)*i)
    elif b==0:
        break

print(count)   