import os
from twilio.rest import Client
from dotenv import load_dotenv

env_path = '/path/to/the/variable/folder/.env'
load_dotenv(dotenv_path=env_path)

class FlightNotifs:
    def __init__(self):
        self.client = Client(os.environ.get('TWILIO_ACCOUNT_SID'), os.environ.get('TWILIO_AUTH_TOKEN'))
        
    def send_sms(self, message_body):
        message = self.client.messages.create(from_=os.environ.get('TWILIO_VIRTUAL_NUMBER'), body=message_body, to=os.environ.get('TWILIO_VERIFIED_NUMBER'))
        
        print(message.sid)
        
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(from_=f"whatsapp:{os.environ.get('TWILIO_WHATSAPP_NUMBER')}", body=message_body, to=f"whatsapp:{os.environ.get('TWILIO_VERIFIED_NUMBER')}")
        
        print(message.sid)