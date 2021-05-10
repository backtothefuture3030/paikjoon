
a = int(input())
i = 666
b = 0
while True:
    num = str(i)
    for j in range(0,len(num)-2):
        if str(i)[j:j+3] == "666":
            b = b+1
            break
    if b == a :
        break
    else:
        i += 1

print(str(i))