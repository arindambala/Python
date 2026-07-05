# Day 35 - 100 Days of Code

LAT = 20.296059
LLT = 85.824539

OWM_API = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = '_!@#$%^&*()+_'

import requests

print(f"\n---- Authenticate ^ Keys ----\n")

parameters = {
    'lat': LAT,
    'lon': LLT,
    'appid': API_KEY,
}

response = requests.get(OWM_API, params=parameters)
print(response.json())