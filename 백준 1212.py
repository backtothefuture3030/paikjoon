a = input()
b = []
total = ''
for i in a:
    b.append(str(bin(int(i)))[2:])
if a=='0':
    print(0)
    exit()
if b[0] == '0':
    pass
else:
    total+=b[0]
b.pop(0)


for j in b:
    if len(j)==1:
        j = '00'+j
        total+=j
    elif len(j)==2:
        j = '0'+j
        total+=j
    else:
        total+=j

print(total)