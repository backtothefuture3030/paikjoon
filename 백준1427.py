a = input()
A = list(' '.join(a).split())
b = []
for i in A:
    b.append(int(i))
b.sort(reverse=True)
for i in b:
    print(str(i),end='')



