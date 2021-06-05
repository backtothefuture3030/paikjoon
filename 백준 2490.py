
for i in range(3):
    yoot = list(input().split())
    a = yoot.count('1')
    if a==4:
        print("E")
    elif a==3:
        print('A')
    elif a==2:
        print('B')
    elif a==1:
        print('C')
    else:
        print('D')


'''
while True:
    try:
        print(input())
    except EOFError:
        break
'''