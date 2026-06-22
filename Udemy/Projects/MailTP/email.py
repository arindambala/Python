# Day 32 - 100 Days of Code

import smtplib

mail = '_address_@gmail.com'
key = '_!@#$%^&*()+_'

connection = smtplib.SMTP('smtp.gmail.com') # Depends on the information about the particular domain

with connection as connect:
    connect.starttls()

    connect.login(user=mail, password=key)
    connect.sendmail(from_addr=mail, to_addrs='_address_@live.com', msg='Subject:Hello\n\nBruh')

    #connect.close()