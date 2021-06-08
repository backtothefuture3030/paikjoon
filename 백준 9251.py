A = input()
B = input()
a = len(A)
b = len(B)
count = [[0] * (b + 1) for _ in range(a + 1)]

for i in range(1,a+1):
    for j in range(1,b+1):
        if A[i-1] == B[j-1]:
            count[i][j] = count[i-1][j-1] +1
        else:
            count[i][j] = max(count[i-1][j],count[i][j-1])
            
print(count[-1][-1])
