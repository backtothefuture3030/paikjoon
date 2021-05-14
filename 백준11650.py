

q = int(input())
i=0
w = []
while i<q:
    i+=1
    x,y = map(int,input().split())
    w.append((x,y))

w.sort()
for i in range(len(w)):
    print(w[i][0], w[i][1])


