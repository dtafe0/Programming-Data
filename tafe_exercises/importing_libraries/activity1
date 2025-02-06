import calendar
from random import randint as rint
from datetime import time, date

theTime = time(22, 46, 15, 200)
theTime = time(microsecond = 200, second = 15, minute = 46, hour = 22)
theTime = theTime.replace(hour = 12, minute = 24)
print("The time is ", theTime)

for i in range(10):
    print(rint(1,25))

c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2017,1,0,0)
print(st)

for i in c.itermonthdays(2017,8):
    print(i)


# c = calendar.HTMLCalendar(calendar.SUNDAY)
# st = c.formatmonth(2017,1)
# print(st)

for m in range(1,13):
    cal = calendar.monthcalendar(2019,m)
    week1 = cal[0]
    week2 = cal[1]
    if week1[calendar.FRIDAY] != 0:
        meetday = week1[calendar.FRIDAY]
    else:
        meetday = week2[calendar.FRIDAY]
    print("%10s %2d" % (calendar.month_name[m], meetday))

theDate = date(2019,2,24)
print("The date is: ", theDate)

theDate = theDate.replace(month = 6, year = 2017)
yr = theDate.year
mth = theDate.month
dy = theDate.day
print("You were born on the ", dy, " day of the ", mth, " month in the year ", yr)

todaysDate = date.today()
print("Today''s date is: ", todaysDate)

