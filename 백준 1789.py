

n = int(input())
count=0
if n==1:
    print(1)
    exit()
for i in range(1,n):
    if n<=i:
        break
    count+=1
    n-=i

print(count)


'''
s = int(input())
n = 1
while n*(n+1)/2 <=s:
    n+=1
print(n-1)

'''