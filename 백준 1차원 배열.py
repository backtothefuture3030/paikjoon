'''
a = int(input())
b = list(map(int,input().split()))
if a==len(b):
    print(min(b),max(b))
    '''

'''
i = 0
w = 9
a = []
while i<w:
    i+=1
    b = int(input())
    a.append(b)
print(max(a))
print(a.index(max(a))+1)
    '''


'''
A = int(input())
B = int(input())
C = int(input())
D = A*B*C
for i in range(10):
    print(str(D).count(str(i)))'''


'''
i = 0
w = 10
b = []
while i<w:
    i+=1
    a = int(input())
    b.append(a%42)

print(len(set(b)))
'''

'''
a = int(input())
b = list(map(int,input().split()))
c = []
if a==len(b):
    for i in b:
        i = i/max(b)*100
        c.append(i)
print(sum(c)/a)
'''