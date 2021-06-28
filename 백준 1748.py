
a = int(input())
b = len(str(a))
count = 0 
if a<10:
    print(a)
elif 100>a>10:
    count+=9
    count+=(a-9)*b
    print(count)
else:
    #if a%(int('1'+'0'*(b-1))==0:

    count+=9
    total='9'+'0'*(b-2)
    if a-int(total)>0:
        count+=(int(total)*(b-1))
    z = '1'+'0'*(b-1)
    count+=(a-int(z)+1)*b
    print(count)
'''
n = input()
n_len = len(n) - 1
c = 0
i = 0
while i < n_len:
    c += 9 * (10 ** i) * (i + 1)
    i += 1
c += ((int(n) - (10 ** n_len)) + 1) * (n_len + 1)
print(c)
'''