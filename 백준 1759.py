from itertools import combinations

k,j = map(int,input().split())
a = list(input().split())
b = list(combinations(a,k))
alph = ['a','e','i','o','u']
bat = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

e = []
if len(a)==j:
    for i in b:
        c=''
        for j in sorted(i):
            c+=j
        e.append(c)
    e.sort()
    for q in e:
        count = 0
        total = 0
        for l in q:
            if l in alph:
                count+=1
            if l in bat:
                total+=1
        if total>1 and count>0:
            print(q)

