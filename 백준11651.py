import sys

q = int(sys.stdin.readline())

i=0
w = []
while i<q:
    i+=1
    x,y = map(int,sys.stdin.readline().split())
    w.append((y,x))

w.sort()
for i in range(len(w)):
    print(w[i][1], w[i][0])

