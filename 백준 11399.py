a = int(input())

b = list(map(int,input().split()))

if a == len(b):
    b.sort()
    total = 0
    sum = 0
    for i in b:
        sum+=i
        total+=sum

print(total)
        


