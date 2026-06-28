# Day 33 - 100 Days of Code

import requests

print(f"\n---- ISS ^ Locator ----\n")

response = requests.get(url='http://api.open-notify.org/iss-now.json')