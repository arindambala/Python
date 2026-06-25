# Day 32 - 100 Days of Code

import smtplib
import datetime as dt

mail = '_address_@gmail.com'
key = '_!@#$%^&*()+_' # In accordance with the app password generation for the respective domain

''' connection = smtplib.SMTP('smtp.gmail.com') # Depends on the information about the particular domain

with connection as connect:
    connect.starttls()

    connect.login(user=mail, password=key)
    connect.sendmail(from_addr=mail, to_addrs='_address_@live.com', msg='Subject:Hello\n\nBruh') # Change with respect to the domain

    #connect.close() '''

now = dt.datetime.now()