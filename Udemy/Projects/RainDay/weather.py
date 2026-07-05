# Day 35 - 100 Days of Code

LAT = 20.296059
LLT = 85.824539

import requests
from twilio.rest import Client

OWM_API = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = '_!@#$%^&*()+_'

ACCOUNT_SID = '$ZhjGSq!15xN)da(5mSgnS9+qPeO4IT!H$)g2gDxjm1n1'
AUTH_TOKEN = '_!@#$%^&*()+!@#$%^&*()+!@#$%^&*()+_'

print(f"\n---- Authenticate ^ Keys ----\n")

parameters = {
    'lat': LAT,
    'lon': LLT,
    'cnt': 4,
    'appid': API_KEY,
}

response = requests.get(OWM_API, params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for hour_data in weather_data['list']:
    weather_status = hour_data['weather'][0]['id']
    if int(weather_status) < 700:
        will_rain = True
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(body='Bring thy umbrella!☔', from_='+0123456789', to='+9876543210') # whatsapp:TWILIO_WHATSAPP_NUMBER | WhatsApp
    
    print(message.status)