import os
import requests
from dotenv import load_dotenv

env_path = '/path/to/the/variable/folder/.env'
load_dotenv(dotenv_path=env_path)

class Task:
    def __init__(self):
        self.api_endpoint = os.environ.get('SHEETY_ENDPOINT')
        self.api_key = os.environ.get('BEARER_KEY')
        self.user_endpoint = os.environ.get('USER_ENDPOINT')
        
        self.auth = {
            'Authorization': f'Bearer {self.api_key}'
        }
        
        self.destination_data = {}
        self.customer_data = {}
    
    def get_destination_data(self):
        response = requests.get(url=self.api_endpoint, headers=self.auth)
        
        data = response.json()
        # print(data)
        
        self.destination_data = data['prices']
        return self.destination_data
    
    def update_least_price(self, row_id, updated_price):
        updated_data = {
            'price': {
                'lowestPrice': updated_price,
            }
        }
        requests.put(url=f'{self.api_endpoint}/{row_id}', json=updated_data, headers=self.auth)
    
    def get_customer_emails(self):
        response = requests.get(url=self.user_endpoint, headers=self.auth)
        
        data = response.json()
        #print(data)
        
        self.customer_data = data['users']
        return self.customer_data