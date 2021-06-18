a, b = map(int,input().split())

if a>0 and b>0 :
    print(abs(a-b))
elif (a>0 and b<0) or (a<0 and b>0):
    print(abs(-a+b))
elif a<0 and b<0 and a>b:
    print(abs(b-a))
else:
    print(abs(a-b))
