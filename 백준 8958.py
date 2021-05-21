
i = int(input())
w = 0
while w<i:
    w+=1
    a = input()
    stack = 0
    count = 0
    for j in range(len(a)):
        if a[j]=="O" and stack>0:
            count+=(stack+1)
            stack+=1
        elif a[j]=="O":
            count+=1
            stack+=1
        elif a[j]=="X":
            stack=0
    print(count)
