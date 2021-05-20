import sys
a = int(sys.stdin.readline())
i = 0
while i<a:
    i+=1
    q,w = map(int,sys.stdin.readline().split())
    print(q+w)