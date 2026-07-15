# Day 47 - 100 Days of Code

import os
from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv

env_path = '/path/to/the/variable/folder/.env'
load_dotenv(dotenv_path=env_path)

MY_MAIL = os.environ.get('MAIL_ID')
MY_PASSWORD = os.environ.get('MAIL_KEY')
SMTP_ADDR = os.environ.get('SMTP_ADDRESS')

URL = 'https://store.steampowered.com/search/?specials=1'

BUY_PRICE = 75

# Mimic Web Browser
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

print(f'\n---- Automate ^ Sale ----\n')

try:
    response = requests.get(URL, headers=header)
    response.raise_for_status()
    
    website_html = response.text
    soup = BeautifulSoup(website_html, 'html.parser')
    # print(soup.prettify())
    
    discounted_games = soup.find_all(name='a', class_='search_result_row')
    
    deals_found = []
    
    print('\n---- Games at discount | 75% or more : ----\n')
    
    for game in discounted_games:
        discount = game.find('div', class_='discount_pct')
        
        if discount:
            discount_text = discount.text.strip().replace('-', '').replace('%', '')

            try:
                discount_val = int(discount_text)
                
                if discount_val >= BUY_PRICE:
                    title = game.find('span', class_='title').text.strip()
                    sale_price = game.find('div', class_='discount_final_price').text.strip()
                    original_price = game.find('div', class_='discount_original_price').text.strip()
                    
                    scrap_deals = f'🎮 {title} is {discount_val}% off! (Now: {sale_price}) | (Was: {original_price})'
                    
                    deals_found.append(scrap_deals)

            except ValueError:
                continue
    
    if deals_found:
        subject = '❗ Heavy Steam Discounts!'
        body = 'Hey! Here are the Steam deals matching your criteria....\n\n'
        body += '\n'.join(deals_found)
        
        raw_message = f'Subject: {subject}\n\n{body}'
        
        with smtplib.SMTP(SMTP_ADDR, 587) as connection:
            connection.starttls()
            
            connection.login(MY_MAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_MAIL, to_addrs=MY_MAIL, msg=raw_message.encode('utf-8'))
        
        print('✅ Email sent successfully!')
    else:
        print('❌ No games found with 75% off or more today!')

except requests.exceptions.HTTPError as err:
    print(f'HTTP Error : {err}')

except Exception as err:
    print(f'An unexpected error occured : {err}')