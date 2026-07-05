# Day 35 - 100 Days of Code

LAT = 20.296059
LLT = 85.824539

import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

env_path = '/path/to/the/variable/folder/.env'
load_dotenv(dotenv_path=env_path)

OWM_API = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = os.environ.get('OWM_API_KEY')

ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

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