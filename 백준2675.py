a = int(input())
i = 0

while i<a:
    i+=1
    w=''
    n, p = input().split()
    r = []
    for j in p:
        r.append(j*int(n))
    for k in r:
        w+=k 
    print(w)