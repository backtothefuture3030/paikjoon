n = int(input())

total=0
a = list(map(int,input().split()))
b = list(map(int,input().split()))

if len(a)==len(b)==n:
    a.sort(reverse=True)
    b.sort()
    w = 0
    while w<len(a):
        total+=a[w]*b[w]
        w+=1
print(total)


