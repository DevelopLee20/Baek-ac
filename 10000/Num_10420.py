# day = int(input()) + 1

# year = 2014
# month = 3

# all_days = 366
# while day >= all_days:
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         all_days = 366
#     else:
#         all_days = 365
    
#     day -= all_days
#     year += 1

# month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     month_days[1] = 29

# while day > month_days[month]:
#     day -= month_days[month]
#     month += 1

#     if month > 11:
#         year += 1
#         month = 0

#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             month_days[1] = 29
#         else:
#             month_days[1] = 28

# print(f"{year}-{month+1:02d}-{day:02d}")

from datetime import timedelta, datetime

day = datetime(2014, 4, 1)
print(str(day + timedelta(days=int(input()))).split(" ")[0])
