


a = int(input())
def hanoi(a,b,c,d):
    if a==1:
        print(b,c)
        return
    hanoi(a-1,b,d,c)
    print(b,c)
    hanoi(a-1,d,c,b)

sum=1
for i in range(a-1):
    sum = sum * 2 +1
print(sum)
hanoi(a,1,3,2)  