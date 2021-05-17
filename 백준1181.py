import sys
q = int(sys.stdin.readline())
i = 0
a = []
while i<q:
    i+=1
    w = sys.stdin.readline()[:-1]
    a.append((len(w),w))

a = list(set(a))
a.sort()
r = []

for i in range(len(a)):
    print(a[i][1])




