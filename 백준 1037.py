import sys

a = int(sys.stdin.readline())

b = list(map(int,sys.stdin.readline().split()))

if len(b)==a:
    b.sort()
    if len(b)==1:
        total=b[0]**2
    else:
        total = b[0]*b[-1]
    print(total)
