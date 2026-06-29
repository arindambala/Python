# Day 33 - 100 Days of Code

import requests

print(f"\n---- ISS ^ Locator ----\n")

response = requests.get(url='http://api.open-notify.org/iss-now.json')
print(response.status_code) # print(response)

'''
1XX - Hold On
2XX - Here You Go
3XX - Go Away
4XX - You Screwed Up
5XX - I Screwed Up
'''

# if response.status_code == 404:
#     raise Exception('Does not exist!')
# elif response.status_code == 401:
#     raise Exception('Unauthorised access!')

response.raise_for_status()

data = response.json()
print(data)