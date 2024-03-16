import datetime as dt
month_dict = {'January': 1, 'February': 2, 'March': 3,
              'April': 4, 'May': 5, 'June': 6,
              'July': 7, 'August': 8, 'September': 9,
              'October': 10, 'November': 11, 'December': 12}



a = input()
month_day = a.split(",")[0]
year_time = a.split(",")[1]
month, day = month_day.split()
year, time = year_time.split()

month = month_dict[month]
hour = time.split(":")[0]
minute = time.split(":")[1]
year, month, day, hour, minute = int(year), int(month), int(day), int(hour), int(minute)

a = dt.datetime(year, month, day, hour, minute)
yoon_year = 0
if a.year % 400 == 0:
    yoon_year += 1
elif a.year % 4 == 0 and a.year % 100 != 0:
    yoon_year += 1
else:
    yoon_year = 0


b = dt.datetime(year+1, 1, 1, 0, 0, 0)
c = b-a

ans = (1 - ((c.days + (c.seconds/86400))) / (365 + yoon_year)) * 100
print(ans)

