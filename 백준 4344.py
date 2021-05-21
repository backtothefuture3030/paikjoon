a = int(input())
w = 0

while w<a:
    w+=1
    b = list(map(int,input().split()))
    count=0
    if b[0]==len(b[1:]):
        e = sum(b[1:])/b[0]
        for i in range(1,len(b)):
            if b[i]>e:
                count+=1
    rate = count/b[0]*100
    print(f'{rate:.3f}%')