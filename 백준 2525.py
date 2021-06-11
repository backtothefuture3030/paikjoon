h, m = map(int,input().split())
t = int(input())

if t>=60:
    h+=(t//60)
    m+=(t%60)
    if m>=60:
        h+=(m//60)
        m-=60
else:
    m+=t
    if m>=60:
        h+=(m//60)
        m-=60

if h>=24:
    h-=24


print(h,m)