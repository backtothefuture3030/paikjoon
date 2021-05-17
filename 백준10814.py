import sys
q = int(sys.stdin.readline())
i = 0
w = []
while i<q:
    a,b = sys.stdin.readline()[:-1].split()
    w.append((int(a),b,i))
    i+=1
    
w.sort(key=lambda x: int(x[0]))
for i in range(len(w)-1):
    if w[i][0]==w[i+1][0] and w[i][2]>w[i+1][2]:
        t = w[i]
        w[i] = w[i+1]
        w[i+1] = t

for i in range(len(w)):
    print(w[i][0], w[i][1])
