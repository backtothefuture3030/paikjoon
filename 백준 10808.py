count = [0]*26
a = input()
for i in a:
    count[ord(i)-97]+=1

for j in count:
    print(j, end = ' ')