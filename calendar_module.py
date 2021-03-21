import calendar

date = input()
month, day, year = map(int, date.split(' '))

day = calendar.weekday(year, month, day)
day_name = ""

if day == 0:
    print("MONDAY")
elif day == 1:
    print("TUESDAY")
elif day == 2:
    print("WEDNESDAY")
elif day == 3:
    print("THURSDAY")
elif day == 4:
    print("FRIDAY")
elif day == 5:
    print("SATURDAY")
elif day == 6:
    print("SUNDAY")
