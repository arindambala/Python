# Day 38 - 100 Days Of Code

import os
import requests
from datetime import datetime
from dotenv import load_dotenv

print(f'\n---- Workout ^ Tracker ----\n')

env_path = '/path/to/the/variable/folder/.env'
load_dotenv(dotenv_path=env_path)

APP_ID = os.environ.get('NUEX_ID')
API_KEY = os.environ.get('NUEX_KEY')