
b = int(input())
a = input()
i = 0
c = []
for i in range(b):
    c.append(int(a[i:i+1]))
    i+=1
print(sum(c))

