def domino():
    count=0
    a = int(input())
    if a < 100:
        print(a)
    else:
        for i in range(100,a+1):
            b = str(i)[0]
            c = str(i)[1]
            d = str(i)[2]
            if int(b)-int(c) == int(c)-int(d):
                count+=1
        print(count+99)

domino()







