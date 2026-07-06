# Day 36 - 100 Days of Code

print(f'\n---- Stock ^ News ----\n')

import requests

STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tesla Inc.'

STOCK_ENDPOINT = 'https://www.alphadvantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

STOCK_API_KEY = '_!@#$%^&*()+__!@#$%^&*()+_'
NEWS_API_KEY = '_!@#$%^&*()+__!@#$%^&*()+_'

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

price_difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(price_difference)

diff_percent = (price_difference / float(yesterday_closing_price)) * 100
print(diff_percent)

if diff_percent > 5:
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