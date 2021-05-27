a,b = map(int,input().split())

box = []
mini = []

for _ in range(a):
    box.append(input())

for i in range(a-7):
    for j in range(b-7):
        idx1 = 0
        idx2 = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2==0:
                    if box[k][l] !='W' : idx1+=1
                    if box[k][l] !='B': idx2+=1
                else:
                    if box[k][l] !='B': idx1+=1
                    if box[k][l] !='W': idx2+=1
        mini.append(idx1)
        mini.append(idx2)
print(min(mini))

