M = int(input())
N = int(input())
a = []
i = 1
while i**2 <= N:
    if M<= i**2 <= N:
        a.append(i**2)
    i+=1
if a:
    print(sum(a))
    print(min(a))
else:
    print(-1)