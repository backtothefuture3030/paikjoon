
n = int(input())
words = []
for i in range(n):
    words.append(input())
dic = {}
for word in words:
    k = len(word)-1
    for j in word:
        if j in dic:
            dic[j]+=pow(10,k)
        else:
            dic[j]=pow(10,k)
        k-=1
nums = []

for value in dic.values():
    nums.append(value)

nums.sort(reverse=True)
total = 0
a = 9
for i in range(len(nums)):
    total+=nums[i]*a
    a-=1
print(total)



