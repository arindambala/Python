# Day 33 - 100 Days of Code

LAT = 20.296059
LLT = 85.824539

MAIL = '_address_@gmail.com'
KEY = '_!@#$%^&*()+_'

from datetime import datetime
from zoneinfo import ZoneInfo
import requests
import smtplib

print(f"\n---- ISS ^ Locator ----\n")

def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    # print(response.status_code) | print(response)

    '''
    1XX - Hold On
    2XX - Here You Go
    3XX - Go Away
    4XX - You Screwed Up
    5XX - I Screwed Up
    '''

    # if response.status_code == 404:
    #     raise Exception('Does not exist!')
    # elif response.status_code == 401:
    #     raise Exception('Unauthorised access!')

    response.raise_for_status()

    data = response.json()['iss_position'] # Pinpoint
    # print(data)

    iss_lat = float(data['latitude'])
    iss_lon = float(data['longitude'])

    # iss_pos = (lat, lon)
    # print(iss_pos)

    if LAT-5 <= iss_lat <= LAT+5 and LLT-5 <= iss_lon <= LLT+5:
        return True
    return False

def is_night():
    parameters = {
        'lat': LAT,
        'lng': LLT,
        'formatted': 0,
    }

    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()

    data = response.json()
    # print(data)
    
    local_tz = ZoneInfo('Asia/Kolkata')

    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']

    sunrise_utc = datetime.fromisoformat(sunrise)
    sunset_utc = datetime.fromisoformat(sunset)

    sunrise_ist = sunrise_utc.astimezone(local_tz)
    sunset_ist = sunset_utc.astimezone(local_tz)

    curr_time = datetime.now(local_tz)
    
    if curr_time <= sunrise_ist or curr_time >= sunset_ist:
        return True
    return False

if is_iss_overhead() and is_night():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        
        connection.login(MAIL, KEY)
        connection.sendmail(from_addr=MAIL, to_addrs=MAIL, msg='Subject:LOOK UP!🪐\n\nThe International Space Station (ISS) is up above in the sky!')