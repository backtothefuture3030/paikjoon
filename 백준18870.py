import sys
q = int(sys.stdin.readline())


a = list(map(int, input().split()))
if q == len(a):
    b = sorted(list(set(a)))
    c = {}
    for i in range(len(b)):
        c[b[i]] = i
    for i in a:
        print(c[i],end=' ')
