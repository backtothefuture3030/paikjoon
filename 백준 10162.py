
n = int(input())

Acount = 0
Bcount = 0
Ccount = 0

if n%10 != 0 :
    print(-1)
else:
    Acount = n//300
    Bcount = (n%300)//60
    Ccount = (n%300)%60//10
    print(Acount,Bcount,Ccount)
