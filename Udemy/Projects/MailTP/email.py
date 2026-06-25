# Day 32 - 100 Days of Code

import smtplib
import datetime as dt
import random

mail = '_address_@gmail.com'
key = '_!@#$%^&*()+_' # In accordance with the app password generation for the respective domain

''' connection = smtplib.SMTP('smtp.gmail.com') # Depends on the information about the particular domain

with connection as connect:
    connect.starttls()

    connect.login(user=mail, password=key)
    connect.sendmail(from_addr=mail, to_addrs='_address_@live.com', msg='Subject:Hello\n\nBruh') # Change with respect to the domain

    #connect.close() '''

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open('quotes.txt') as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes)
    
    # print(quote)
    
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        
        connection.login(mail, key)
        connection.sendmail(from_addr=mail, to_addrs=mail, msg=f'Subject:Monday Motivation\n\n{quote}')