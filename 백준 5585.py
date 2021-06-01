
n = 1000 - int(input())

nums = [500,100,50,10,5,1]
total = 0

for i in nums:
    total += n//i
    n%=i
print(total) 
