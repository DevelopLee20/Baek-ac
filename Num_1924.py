week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
month = [31,28,31,30,31,30,31,31,30,31,30,31]

a, b = map(int, input().split(" "))

day = b
for i in range(0,a-1):
    day = day + month[i]
    
print(week[day%len(week)])