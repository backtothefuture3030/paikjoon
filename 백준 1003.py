

a = int(input())
zero = [1,0,1]
one = [0,1,1]
def fibonacci(n):
    lena = len(zero)
    if lena <= n:
        for i in range(lena, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("{} {}".format(zero[n],one[n]))

q = 0
while q<a:
    q+=1
    num = int(input())
    fibonacci(num)

        
