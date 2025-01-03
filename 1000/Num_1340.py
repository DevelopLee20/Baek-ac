# 입력
month, day, year, time = input().split()

# 입력 값 전처리
hour, minute = map(int, time.split(":"))
day = int(day[:-1]) - 1
year = int(year)

# 윤년 처리
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total_days = 365
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    days[1] += 1
    total_days += 1

# 최종 계산
month_int = months.index(month)
sum_days = sum(days[:month_int])
total_minute = total_days * 24 * 60
minute = (sum_days + day) * 24 * 60 + hour * 60 + minute

print(minute / total_minute * 100)
