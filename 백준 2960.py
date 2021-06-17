N, K = map(int,input().split())

a = []
b = []
for i in range(2,N+1):
    a.append(i)
    b.append(i)

count = 0 

for j in b:
    for k in a:
        if k%j==0:
            a.remove(k)
            count+=1
            if count==K:
                print(k)
