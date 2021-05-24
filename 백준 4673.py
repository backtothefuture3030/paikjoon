
def self():
    a = list(range(1,10000))
    for i in range(1,10000):
        total=0
        total+=i
        for j in str(i):
            total+=int(j)
        if total in a:
            a.remove(total)
    for k in a:
        print(k)
self()





        
