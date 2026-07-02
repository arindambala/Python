# Day 33 - 100 Days of Code

LAT = 20.296059
LLT = 85.824539

from datetime import datetime
from zoneinfo import ZoneInfo
import requests

print(f"\n---- Sunrise ^ Sunset ----\n")

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

print(f'BBS Rise : {sunrise_ist.strftime('%I:%M:%S %p')} | BBS Set : {sunset_ist.strftime('%I:%M:%S %p')}')

curr_time = datetime.now(local_tz)
print(f'BBS Current : {curr_time.strftime('%I:%M:%S %p')}')