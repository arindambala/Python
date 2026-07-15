# Day 48 - 100 Days of Code

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://ozh.github.io/cookieclicker/')

sleep(3)

try:
    english_select = driver.find_element(By.ID, 'langSelect-EN')
    english_select.click()
    sleep(3)
except NoSuchElementException:
    print('Language not found!')

sleep(2)

wait_time = 2
timeout = time() + wait_time
five_min = time() + 60 * 5

cookie_button = driver.find_element(By.ID, value="bigCookie")

while True:
    cookie_button.click()
    
    if time() > timeout:
        upgrades = driver.find_elements(By.CSS_SELECTOR, value='div.product.unlocked.enabled')
        
        if upgrades:
            most_expensive = upgrades[-1]
            
            try:
                most_expensive.click()
            except Exception:
                pass
            
        timeout = time() + wait_time
    
    if time() > five_min:
        cookies = driver.find_element(By.ID, value='cookies')
        cookie_count = int(cookies.text.split()[0].replace(',', ''))
        print(f'Cookies : {cookie_count}!')
        break

driver.quit()