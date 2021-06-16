
N = int(input())
total = 1
for i in range(1,N+1):
    total *= i 
count = 0
for i in range(len(str(total))-1,-1,-1):
    if str(total)[i] == '0':
        count+=1
        pass
    else:
        print(count)
        break