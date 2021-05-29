
num = input()
numbers = []
n = []
for i,j in enumerate(num):
    if j=="-":
        n.append(i)

n.append(len(num))
A = int(num[:n[0]])

for i in range(0,len(n)-1):
    numbers.append(num[n[i]+1:n[i+1]])

t= []
q = []
for i in numbers:
    w = list(map(int,i.split("+")))
    t.append(w)
for i in t:
    q.append(sum(i))

total = 0
for i in t:
    for j in i:
        total+=j

print(A - total)
'''
a = input().split('-')
num = []
for i in a:
    count = 0
    b = i.split("+")
    for j in b:
        count += int(j)
    num.append(count)
n = num[0]
for i in range(1,len(num)):
    n-= num[i]
print(n)
    
'''

