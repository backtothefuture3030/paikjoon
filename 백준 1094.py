a = [64,32,16,8,4,2,1]
n = int(input())

total = 0
count = 0
for i in a:
    if n-i>0:
        n-=i
        count+=1
    elif n-i==0:
        count+=1
        break
print(count)