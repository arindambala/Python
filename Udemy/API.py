# Day 33 - 100 Days of Code

import requests

print(f"\n---- ISS ^ Locator ----\n")

response = requests.get(url='http://api.open-notify.org/iss-now.json')
# print(response)

'''
1XX - Hold On
2XX - Here You G
3XX - Go Away
4XX - You Screwed Up
5XX - I Screwed Up
'''