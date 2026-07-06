# Day 36 - 100 Days of Code

print(f'\n---- Stock ^ News ----\n')

import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

env_path = '/path/to/the/variable/folder/.env'
load_dotenv(dotenv_path=env_path)

STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tesla Inc.'

STOCK_ENDPOINT = 'https://www.alphadvantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

STOCK_API_KEY = os.environ.get('AADV_API_KEY')
NEWS_API_KEY = os.environ.get('NORG_API_KEY')

ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()

data = stock_response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)

price_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
# print(price_difference)
up_down = '📈' if price_difference > 0 else '📉'

diff_percent = round((price_difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

if abs(diff_percent) > 5:
    # print('Stock News!')
    news_parameters = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
    }
    
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    
    articles = news_response.json()['articles']
    news_articles = articles[:3]
    print(news_articles)
    
    data_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}% \nHeadline: {article['title']} \nBrief: {article['description']}" for article in news_articles]
    
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    for article_text in data_articles:
        message = client.messages.create(body=article_text, from_='+0123456789', to='+9876543210')
    
        print(message.status)