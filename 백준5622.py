Alpha = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
a = input()
time = 0
for i in range(len(a)):
    for j in Alpha:
        if a[i] in j:
            time += Alpha.index(j)+3
print(time)