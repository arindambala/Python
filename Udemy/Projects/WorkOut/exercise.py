# Day 38 - 100 Days Of Code

import os
import requests
from datetime import datetime
from dotenv import load_dotenv

print(f'\n---- Workout ^ Tracker ----\n')

env_path = '/path/to/the/variable/folder/.env'
load_dotenv(dotenv_path=env_path)

NUEX_ENDPOINT = 'https://app.100daysofpython.dev/v1/nutrition/natural/exercise'

APP_ID = os.environ.get('NUEX_ID')
API_KEY = os.environ.get('NUEX_KEY')

SHEETY_ENDPOINT = 'https://api.sheety.co/username/projectName/sheetName'

ex_text = input('What did you do today? : ')

header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

parameters = {
    'query': ex_text,
    'gender': 'Your Gender',
    'weight_kg': 'Your weight in kg',
    'height_cm': 'Your weight in cm',
    'age': 'Your age',
}

response = requests.post(NUEX_ENDPOINT, json=parameters, headers=header)
data = response.json() # print(response.json())

today = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%X')

for exercise in data['exercises']:
    sheety_config = {
        'workout': {
            'date': today,
            'time': time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }
    
    sheety_response = requests.post(SHEETY_ENDPOINT, json=sheety_config) # No Authentication
    print(sheety_response.text)

''' BASIC AUTHENTICATION '''

BASIC_USERNAME = os.environ['BASIC_ID']
BASIC_PASSWORD = os.environ['BASIC_KEY']

sheety_response = requests.post(SHEETY_ENDPOINT, json=sheety_config, auth=(BASIC_USERNAME, BASIC_PASSWORD)) # HTTP Basic Auth | base64

''' BEARER AUTHENTICATION '''

BEARER_TOKEN = os.environ.get('BEARER_KEY')

bearer_header = {
    'Authorization': f'Bearer {BEARER_TOKEN}'
}

sheety_response = requests.post(SHEETY_ENDPOINT, json=sheety_config, headers=bearer_header) # Token-based security