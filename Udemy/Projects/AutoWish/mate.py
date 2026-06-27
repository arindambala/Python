# Day 32 - 100 Days of Code

mail = '_address_@gmail.com'
key = '_!@#$%^&*()+_'

from datetime import datetime
import pandas
import random
import smtplib

print(f"\n ---- Birthday ^ Wisher ---- \n")

today = datetime.now() # (datetime.now().month, datetime.now().day)
today_tuple = (today.month, today.day)

data = pandas.read_csv('bdays.csv')
bday_dict = {(data_row['month'], data_row['day']) : data_row for (index, data_row) in data.iterrows()}

if today in bday_dict:
    bday_person = bday_dict[today_tuple]
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace('[NAME]', bday_person['name'])
    
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(mail, key)
        
        connection.sendmail(from_addr=mail, to_addrs=bday_person['email'], msg=f'Subject:Happy Birthday!\n\n{contents}')