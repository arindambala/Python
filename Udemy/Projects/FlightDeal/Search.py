import os
import requests
from dotenv import load_dotenv

env_path = '/path/to/the/variable/folder/.env'
load_dotenv(dotenv_path=env_path)

class FlightSearch:
    def __init__(self):
        self.api_endpoint = os.environ.get('SERP_ENDPOINT')
        self.api_key = os.environ.get('SERP_KEY')
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        query = {
            'engine': 'google_flights',
            'departure_id': origin_city_code,
            'arrival_id': destination_city_code,
            'outbound_date': from_time.strftime('%Y-%m-%d'),
            'return_date': to_time.strftime('%Y-%m-%d'),
            'type': '1',
            'adults': '1',
            'currency': 'ISO_code',
            'api_key': self.api_key
        }
        
        if is_direct:
            query['stops'] = '1'
        
        response = requests.get(url=self.api_endpoint, params=query)
        
        if response.status_code != 200:
            print(f'check_flights() response code : {response.status_code}')
            return None
        
        data = response.json()
        if 'error' in data:
            print(f"API error : {data['error']}")
            return None
        
        return data