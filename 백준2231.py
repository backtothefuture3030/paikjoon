a = int(input())
w = 0


if a<=27:
    for i in range(1,a):
        z=i
        for j in range(len(str(i))):
            i+=int(str(z)[j])
        if i==a:
            print(z)
            w=1
            break

else:
    for i in range(a-len(str(a))*9,a):
        z=i
        for j in range(len(str(i))):
            i+=int(str(z)[j])  
        if i==a:
            print(z)
            w=1
            break
if w==0:
    print(0)