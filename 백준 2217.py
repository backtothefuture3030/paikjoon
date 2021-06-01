import sys

a = int(sys.stdin.readline())
w = []
r = []
for i in range(a):
    w.append(int(sys.stdin.readline()))
w.sort(reverse=True)
for j in range(a):
    r.append(w[j]*(j+1))
print(max(r))


'''
r.append(min(w)*len(w))
w.remove(min(w))
while w:
    r.append(min(w)*len(w))
    w.remove(min(w))
print(max(r))

'''
