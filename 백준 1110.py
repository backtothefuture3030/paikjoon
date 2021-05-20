
a = input()
if len(a)<2:
    a = a+"0"
z = a
count=0
while True:
    w = 0
    for i in range(len(a)):
        w+=int(a[i])
    a = a[-1]+str(w)[-1]
    count+=1
    if a==z :
        print(count)
        break
    
