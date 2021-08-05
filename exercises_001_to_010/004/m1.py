year = int(input('输入年:'))
if not (1 <= year):
    print('错误的年份')
    exit(0)
month = int(input('输入月:'))
if not (1 <= month <= 12):
    print('错误的月份')
    exit(0)
day = int(input('输入日:'))
if not (1 <= day <= 31):
    print('错误的天数')
    exit(0)

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

sum_of_day = months[month - 1]
sum_of_day += day

leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum_of_day += 1
print('此日期为当年第 %d 天' % sum_of_day)
