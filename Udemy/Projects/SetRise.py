# Day 33 - 100 Days of Code

LAT = 20.296059
LLT = 85.824539

from datetime import datetime
import requests

print(f"\n---- Sunrise ^ Sunset ----\n")

parameters = {
    'lat': LAT,
    'lng': LLT,
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()
# print(data)
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(f'Rise : {sunrise} | Set : {sunset}')

curr_time = datetime.now()
print(curr_time)