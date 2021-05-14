import sys
from collections import Counter


a = int(sys.stdin.readline())
num = []

for _ in range(a):
    num.append(int(sys.stdin.readline()))

num.sort()
print(round(sum(num)/a))
print(num[a//2])


nums = Counter(num).most_common()
if len(nums) > 1:
    if nums[0][1] == nums[1][1]:
        print(nums[1][0])
    else:
        print(nums[0][0])
else:
    print(nums[0][0])


print(num[-1] - num[0])
