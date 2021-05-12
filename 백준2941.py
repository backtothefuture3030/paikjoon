alpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]
a = input()
count=0
while True:
    for i in alpha:
        while True:
            if i in a:
                if len(i)==3:
                    a = a[:a.find(i)]+" "+a[a.find(i)+3:]
                    count+=1
                if len(i)==2:
                    a = a[:a.find(i)]+" "+a[a.find(i)+2:]
                    count+=1
                elif len(i)==1:
                    a = a[:a.find(i)]+" "+a[a.find(i)+1:]
                    count+=1
            else:
                break
    a = a.replace(" ","")
    b = len(a)
    print(count+b)
    break
    

