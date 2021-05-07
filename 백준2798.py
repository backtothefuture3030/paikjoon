

N,M = map(int,input().split())

a = list(map(int,input().split()))
total =0
b = len(a)
for i in range(0,b):
    for j in range(i+1,b):
        for k in range(j+1,b):
            value = a[i]+a[j]+a[k]
            if value <= M:
                total = max(total,value)
print


'''
from itertools import combinations

if len(a)==N:
    b = list(combinations(a, 3))
    c = [] 

    for i in b:
        c.append(abs(M-sum(i)))
        
    print(M-min(c))
'''