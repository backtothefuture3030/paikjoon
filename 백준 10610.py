
n = list(input())
n.sort(reverse=True)
total = 0
for i in n:
    total+=int(i)
if total%3 != 0 or "0" not in n:
    print(-1)
else:
    print("".join(n))


'''
from itertools import permutations

N = input()

a = list(permutations(N,len(N))) 
b = []

for i in a:
    total = ''
    for j in i:
        total += j 
    b.append(int(total))

c = []
for i in b:
    if i%30==0:
        c.append(i)

if c:
    print(max(c))
else:
    print(-1)
'''