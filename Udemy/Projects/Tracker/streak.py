# Day 37 - 100 Days of Code

import os
import requests
from dotenv import load_dotenv
from datetime import datetime

env_path = '/path/to/the/variable/folder/.env'
load_dotenv(dotenv_path=env_path)

''' HTTP Requests - GET / PUT / POST / DELETE '''

TOKEN = os.environ.get('TOKEN')
USERNAME = os.environ.get('USERNAME')
GRAPH_ID = 'dayW'
TODAY = datetime.now()

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
PIXEL_CREATION_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}'
PIXEL_UPDATION_ENDPOINT = f'{PIXEL_CREATION_ENDPOINT}/{TODAY.strftime('%Y%m%d')}'
PIXEL_DELETION_ENDPOINT = f'{PIXEL_CREATION_ENDPOINT}/{TODAY.strftime('%Y%m%d')}'

print(f'\n---- Habit ^ Tracker ----\n')

''' 1 - CREATE YOUR USER ACCOUNT '''

user_parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
print(response.text)

''' 2 - CREATE A GRAPH DEFINITION '''

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

''' 3 - POST VALUE TO THE GRAPH '''

today = datetime.now()
# print(today)

pixel_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': 'x.xx', # input('Data : ')
}

response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=header)
print(response.text)

''' 4 - UPDATE VALUE OF THE GRAPH '''

update_pixel = {
    'quantity': 'xx.xx',
}

response = requests.put(url=PIXEL_UPDATION_ENDPOINT, json=update_pixel, headers=header)
print(response.text)

'''5 - DELETE VALUE OF THE GRAPH '''

response = requests.delete(url=PIXEL_DELETION_ENDPOINT, headers=header)
print(response.text)