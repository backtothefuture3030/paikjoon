
import sys

A = int(sys.stdin.readline())

for j in range(A):
    N = int(sys.stdin.readline())
    a= [0]*101
    a[1],a[2],a[3]=1,1,1
    for i in range(4,N+1):
        a[i]=a[i-3]+a[i-2]
    print(a[N])

