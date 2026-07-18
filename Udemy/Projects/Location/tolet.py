# Day 53 - 100 Days of Code

import os
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from dotenv import load_dotenv

print(f'\n---- Estate ^ Search ----\n')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=env_path)

URL = os.getenv('SITE_URL')
FORM = os.getenv('FORM_URL')

if not URL or not FORM:
    raise ValueError('\n❗ Error : Site links missing from environment variables (.env file) !')

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

try:
    response = requests.get(URL, headers=header)
    response.raise_for_status()
except RequestException as err:
    print(f'\n❗ Failed to reach the target site : {err}')
    exit(1)

data = response.text

soup = BeautifulSoup(data, 'html.parser')

property_cards = soup.select('.StyledPropertyCardDataWrapper')
property_data = []

print(f'\n\n✔ Scrape Data....Found {len(property_cards)} properties.')

property_price = lambda text: ''.join([char for char in text if char.isdigit() or char in ('$', ',')])

for card in property_cards:
    address_el = card.select_one('address')
    address = address_el.get_text(strip=True).replace(' | ', ' ') if address_el else 'N/A'
    
    price_el = card.select_one('[data-test="property-card-price"]')
    price = 'N/A'
    if price_el:
        raw_price = price_el.get_text(strip=True)
        
        chunk = raw_price.split('+')[0].split(' ')[0]
        price = property_price(chunk)
    
    link_el = card.select_one('a')
    link = link_el['href'] if link_el else 'N/A'
    
    property_data.append({
        'address': address,
        'price': price,
        'link': link,
    })

print('\n\n✔ Data collection successful! Setting up automated browser....')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(FORM)

wait = WebDriverWait(driver, 10)

for idx, prop in enumerate(property_data):
    print(f'\n[{idx + 1}/{len(property_data)}] Submitting : {prop["address"]}')
    
    try:
        form_fields = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[role="listitem"] div[jsmodel]')))
        
        for field in form_fields:
            question_text = field.find_element(By.TAG_NAME, 'span').text.lower()
            input_box = field.find_element(By.TAG_NAME, 'input')
            
            if 'address' in question_text:
                input_box.clear()
                input_box.send_keys(prop['address'])
            elif 'price' in question_text:
                input_box.clear()
                input_box.send_keys(prop['price'])
            elif 'link' in question_text:
                input_box.clear()
                input_box.send_keys(prop['link'])
                
        submit_btn = driver.find_element(By.XPATH, '//span[contains(text(), "Submit") or contains(text(), "Envoyer")]')
        submit_btn.click()
        print('\n✅ Entry logged successfully !')
        
        if idx < len(property_data) - 1:
            response_btn =  wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "formResponse")]')))
            response_btn.click()
            
    except (NoSuchElementException, TimeoutException) as err:
        print(f'\n❌ Structural layout error on form element : {err}')
        continue

print('\n🎉 All property entry transactions completed successfully !')

driver.quit()