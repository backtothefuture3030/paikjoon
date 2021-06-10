import sys

st = sys.stdin.readline()
count =0 
for i in st:
    count+=1
    print(i,end='')
    if count%10==0 and i!=st[-1]:
        print()
