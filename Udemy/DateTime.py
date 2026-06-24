# Day 32 - 100 Days of Code

import datetime as dt

now = dt.datetime.now() # module.className
print(now) # Returns current date and time in yy-mm-dd format & local timezone

year = now.year # month - day - hour etc.
print(year, type(year))

day_of_week = now.weekday()
print(day_of_week) # Starts from Monday - 0