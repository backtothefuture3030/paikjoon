from itertools import combinations
import sys

n = int(sys.stdin.readline())

w = 0
a = []
while w<n:
    w+=1
    a.append(list(map(int,sys.stdin.readline().split())))
b = []


for i in range(len(a)):
   b.append(list(combinations(a[i][1:],2)))

c = []

for j in range(len(b)):
    r = []
    for k in range(len(b[j])):
        for q in range(b[j][k][0],0,-1):
            if b[j][k][1]%q==0 and b[j][k][0]%q==0:
                r.append(q)
                break
    c.append(r)
for t in c:
    print(sum(t))


            
