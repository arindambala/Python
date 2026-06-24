# Day 32 - 100 Days of Code

import datetime as dt

now = dt.datetime.now() # module.className
print(now) # Returns current date and time in yy-mm-dd format & local timezone

year = now.year # month - day - hour etc.
print(year, type(year))

day_of_week = now.weekday()
print(day_of_week) # Starts from Monday - 0

dod = dt.datetime(year=2017, month=3, day=21, hour=9, minute=10) # hour-minute-second - defaulted as 00:00:00
print(dod)