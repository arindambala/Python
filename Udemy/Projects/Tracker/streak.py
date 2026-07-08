# Day 37 - 100 Days of Code

import os
import requests
from dotenv import load_dotenv

env_path = '/path/to/the/variable/folder/.env'
load_dotenv(dotenv_path=env_path)

''' HTTP Requests - GET / PUT / POST / DELETE '''

TOKEN = os.environ.get('TOKEN')
USERNAME = os.environ.get('USERNAME')
GRAPH_ID = 'dayW'

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
PIXEL_CREATION_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}'

print(f'\n---- Habit ^ Tracker ----\n')

''' CREATE YOUR USER ACCOUNT '''

user_parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
print(response.text)

''' CREATE A GRAPH DEFINITION '''

graph_config = {
    'id': GRAPH_ID,
    'name': 'WalkWalk',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}

header = {
    'X-USER-TOKEN': TOKEN
}

response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=header)
print(response.text)

''' POST VALUE TO THE GRAPH '''

pixel_data = {
    'date': 'yyyyMMdd',
    'quantity': 'x.xx',
}

response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=header)
print(response.text)