# Day 32 - 100 Days of Code

from datetime import datetime
import pandas
import random

print(f"\n ---- Birthday ^ Wisher ---- \n")

today = datetime.now() # (datetime.now().month, datetime.now().day)
today_tuple = (today.month, today.day)

data = pandas.read_csv('bdays.csv')
bday_dict = {(data_row['month'], data_row['day']) : data_row for (index, data_row) in data.iterrows()}

if today in bday_dict:
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'