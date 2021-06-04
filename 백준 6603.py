from itertools import combinations


while True:
    a = list(map(int,input().split()))
    if a[0]==0:
        break
    elif a[0] == len(a)-1:
        c = list(combinations(a[1:],6))
    for i in c:
        for j in i:
            print(j,end=' ')
        print()
    print()