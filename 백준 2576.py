a = []
for i in range(7):
    a.append(int(input()))

b = []
for j in a:
    if j%2==1:
        b.append(j)
if len(b)>0:
    print(sum(b))
    print(min(b))
else:
    print(-1)

