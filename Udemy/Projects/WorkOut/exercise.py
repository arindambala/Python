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
print(response.json())