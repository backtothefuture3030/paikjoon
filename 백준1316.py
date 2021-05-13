
b = int(input())
q=0
count=0
while q<b:
    q+=1
    a = input()
    w = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j] and i+1==j:
                break
            elif a[i]==a[j] and i+1 != j:
                w=1
                break
    if w!=1:
        count+=1
print(count)
        

