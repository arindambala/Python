# Day 32 - 100 Days of Code

import smtplib

mail = '_address_@gmail.com'

connect = smtplib.SMTP('smtp.gmail.com') # Depends on the information about the particular domain
connect.starttls()