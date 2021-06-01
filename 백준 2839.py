n = int(input())
a = 5
b = 3
total = 0
while True:
    if n<a:
        break
    else:
        n-=a
        total+=1
if total==0 and b<n<a:
    print(-1)
elif n==0:
    print(total)
elif n%b!=0:
    while n%b !=0:
        n+=a
        total-=1
    total+=(n//b)
    print(total)
elif n%b==0:
    total+=(n//b)
    print(total)
    


