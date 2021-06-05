
month,day = map(int,input().split())
days = [31,28,31,30,31,30,31,31,30,31,30,31]
total = 0
today = ['SUN','MON','TUE','WED','THU','FRI','SAT']
if month == 1:
    total+=day
else:
    total+=day
    for i in days[:month-1]:
        total+=i
print(today[total%7])