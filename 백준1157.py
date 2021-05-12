a = input()
b = a.lower()
c = {}
q = []
for i in b :
    if i in c:
        pass
    else:
        c[i]=b.count(i)

d = {}
for k,v in c.items():   # 키값과 벨류값 뒤집기
    d[v]=k

for i in b:             # 중복된 최대값이 존재하는지 판단
    q.append(c[i])

if max(c.values()) == q.count(max(q)):
    print(d[max(c.values())].upper())
else:
    print("?")


