# Day 33 - 100 Days of Code

LAT = 20.296059
LLT = 85.824539

from datetime import datetime
from zoneinfo import ZoneInfo
import requests

print(f"\n---- ISS ^ Locator ----\n")

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

lon = float(data['longitude'])
lat = float(data['latitude'])

# iss_pos = (lon, lat)
# print(iss_pos)

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