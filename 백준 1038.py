a = int(input()) 
b = 9
count = 9
while True:
    b+=1
    total = 0
    for i in range(len(str(b))-1):
        if str(b)[i]>str(b)[i+1]:
            total+=1
    if total==len(str(b))-1:
        count+=1
    if count==a:
        print(b)
        break

