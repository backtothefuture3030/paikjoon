
from itertools import permutations

a,b = map(int,input().split())
c = []
items = list(permutations(list(range(1,a+1)),b))

for i in items:
    for j in range(len(i)):
        print(i[j],end=' ')
    print()




